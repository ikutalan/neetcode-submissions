class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window = defaultdict(int) # s, and s's counter
        left= 0
        res = 0
        max_count = 0
        for right in range(len(s)):
            window[s[right]] += 1 # increase counter for char
            max_count = max(max_count, window[s[right]])
            while (right - left + 1) - max_count > k:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            res = max(res, right - left + 1)

        return res