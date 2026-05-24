class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for s in strs:
            result = result + s
            result = result + ":;"
        return result
    def decode(self, s: str) -> List[str]:
        answer = []
        start = 0
        for i in range(len(s)):
            if s[i] == ":" and s[i+1] == ";":
                answer.append(s[start:i])
                start = i + 2
        return answer
