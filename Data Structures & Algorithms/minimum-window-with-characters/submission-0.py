class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        sc = Counter(s)
        tc = Counter(t)

        # uses two pointers, l and r
        # starting with l = 0, r = l + len(tc)
        # expand the window until we found the target in the window, then shrink the window size
        l = 0
        matches = 0
        window = defaultdict(int)
        res = ""
        for r in range(len(s)):
            ch = s[r]
            window[ch] += 1
            if ch in tc and window[ch] == tc[ch]:
                matches += 1 # found a match, 
            while matches == len(tc):
                if res == "" or r - l + 1 < len(res):
                    res = s[l:r+1]
                # cut window size
                left_ch = s[l]
                window[left_ch] -= 1
                if left_ch in tc and window[left_ch] < tc[left_ch]:
                    matches -=1 
                l += 1
            
        return res
            