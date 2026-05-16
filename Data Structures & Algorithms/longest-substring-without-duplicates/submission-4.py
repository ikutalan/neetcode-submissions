class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        
        seen = {} # char, last seen index
        left = 0
        res = 0

        for right in range(len(s)):
            if s[right] in seen:
                left = max(seen[s[right]]+1, left)
            seen[s[right]] = right
            res = max(res, right - left + 1)
        return res
