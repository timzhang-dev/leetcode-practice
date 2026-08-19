class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        "zyxyabcdz"
        if not s:
            return 0
        
        max_length = 0
        left = 0
        right = 0
        sett = set()
        while right < len(s):
            if s[right] not in sett:
                length = right - left + 1
                max_length = max(length, max_length)
                sett.add(s[right])
                right += 1
            else:
                while s[left] != s[right]:
                    sett.remove(s[left])
                    left += 1
                sett.remove(s[left])
                left += 1
                
        return max_length

