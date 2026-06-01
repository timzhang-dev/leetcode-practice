class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped = zip(position, speed)
        pair = list(zipped)
        pair.sort(reverse = True)
        stack = []
        for position, speed in pair:
            time = (target - position)/speed
            if stack and time <= stack[-1]:
                continue
            stack.append(time)
        return len(stack)
