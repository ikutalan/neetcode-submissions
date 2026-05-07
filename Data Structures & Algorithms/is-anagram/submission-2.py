class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #把所有字母放到map里，如果两个map相等，return true
        if len(s) != len(t):
            return False
        countS, countT = {},{}
        for i in range(len(s)):
            countS[s[i]] = 1+countS.get(s[i],0)
            countT[t[i]] = 1+countT.get(t[i],0)
        return countS == countT