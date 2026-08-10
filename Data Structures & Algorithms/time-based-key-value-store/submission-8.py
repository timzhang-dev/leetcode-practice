from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.time_map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ""
        n = len(self.time_map[key])
        left = 0
        right = n - 1
        temp = -1
        while left <= right:
            mid = (left + right) // 2
            if self.time_map[key][mid][1]<= timestamp:
                temp = mid
                left = mid + 1
            else:
                right = mid - 1
        if temp != -1:
            return self.time_map[key][temp][0]
        else:
            return ""

