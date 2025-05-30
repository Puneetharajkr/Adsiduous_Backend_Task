from collections import deque

class RateLimiter:
    def __init__(self, limit: int, window: int):
        self.limit = limit
        self.window = window
        self.user_requests = {}

    def allow_request(self, user_id: str, current_time: int) -> bool:
        if user_id not in self.user_requests:
            self.user_requests[user_id] = deque()

        request_times = self.user_requests[user_id]

        # Remove outdated requests outside the time window
        while request_times and current_time - request_times[0] >= self.window:
            request_times.popleft()

        if len(request_times) < self.limit:
            request_times.append(current_time)
            return True
        else:
            return False

# ----------------------------

if __name__ == "__main__":
    rl = RateLimiter(limit=3, window=60)

    print(rl.allow_request("user1", 1))    
    print(rl.allow_request("user1", 20))   
    print(rl.allow_request("user1", 30))   
    
    print(rl.allow_request("user1", 40))   
    print(rl.allow_request("user1", 70))   # True (60 seconds passed since first)
