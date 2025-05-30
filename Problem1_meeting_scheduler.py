def meeting_room_scheduler(meetings):
    if not meetings:
        return (True, 0)

    meetings.sort(key=lambda x: x[0])

    import heapq
    min_heap = []

    for start, end in meetings:
        while min_heap and min_heap[0] <= start:
            heapq.heappop(min_heap)
        heapq.heappush(min_heap, end)

    one_room_enough = len(min_heap) == 1
    min_rooms_required = len(min_heap)

    return (one_room_enough, min_rooms_required)

# -----------------------------

if __name__ == "__main__":
    meetings = [(1, 4), (2, 5), (7, 9)]
    result = meeting_room_scheduler(meetings)
    print(f"Input: {meetings}")
    print(f"Output: {result}")
