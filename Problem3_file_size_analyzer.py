def get_total_size(fs: dict, path: str) -> int:
    def traverse(node):
        total = 0
        for key, value in node.items():
            if isinstance(value, dict):
                total += traverse(value)
            else:
                total += value
        return total

    parts = path.strip('/').split('/')
    current = fs

    for part in parts:
        if part in current:
            current = current[part]
        else:
            return 0

    return traverse(current)

# -----------------------------

if __name__ == "__main__":
    filesystem = {
        "root": {
            "file1.txt": 100,
            "folder1": {
                "file2.txt": 200,
                "folder2": {
                    "file3.txt": 300
                }
            }
        }
    }

    # Example test
    path = "root/folder1"
    result = get_total_size(filesystem, path)
    print(f"Path: {path}")
    print(f"Total size: {result}")
