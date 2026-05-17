class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # what's the window size
        # whats in the window
        # when to re-size the window??

        max_count = 0
        l = 0
        res = 0
        window = defaultdict(int)

        for r in range(len(s)):
            # add right into the window 
            window[s[r]] += 1
            max_count = max(max_count, window[s[r]])
            while r - l + 1 - max_count > k:
                #remove left from window and update l
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    del window[s[l]]
                l += 1
            res = max(res, r - l + 1)
        return res

        # aaababb, 1
        # l
        # r
        # window = {a,1} res = 1 mc = 1
        # aaababb, 1
        # lr
        # window = {a,2} res = 2 mc = 2
        # aaababb, 1
        # l r
        # window = {a,3} res = 3 mc = 3
        # aaababb, 1
        # l  r
        # window = {a,3|b,1} res = 4, mc = 3
        # aaababb, 1
        # l   r
        # window = {a,4|b,1} res = 5, mc = 4
        # aaababb, 1
        # l.   r
        # window = {a,4|b,2} size = 6, mc = 4
        # res = 5
        # aaababb, 1
        #  l   r