class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # use len(s1) to find if there's any len(s1) has the same char and char count
        # window size : len(s1)
        # what's in the window: the string need to be compare
        # when to move the window: the char in string does not have the same char and char count as s1
        if len(s1) > len(s2):
            return False

        l,r = 0, 0
        k = len(s1)
        c1 = Counter(s1)
        c2 = Counter(s2[:len(s1)])
        if c1 == c2:
            return True
        for r in range(len(s1),len(s2)):
            c2[s2[r]] += 1
            c2[s2[r - len(s1)]] -= 1
            if c2[s2[r - len(s1)]] == 0:
                del c2[s2[r - len(s1)]]
            if c2 == c1:
                return True
        return False