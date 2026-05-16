class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # condition window size - most frequent char count <= k
        # what to keep in the window? the most frequent char count
        # what is the window? the sub string

        res = 0
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if s[r] == c:
                    count += 1

                while (r - l + 1) - count > k:
                    # shrink the window size
                    if s[l] == c:
                        count -= 1
                    l += 1
                res = max(r - l + 1, res)
        return res