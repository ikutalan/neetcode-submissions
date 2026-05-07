class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        #把所有字母放到map里，如果两个map相等，return true
        # if len(s) != len(t):
        #     return False
        # countS, countT = {},{}
        # for i in range(len(s)):
        #     countS[s[i]] = 1+countS.get(s[i],0)
        #     countT[t[i]] = 1+countT.get(t[i],0)
        # return countS == countT

        #不用map，也可以用一个size = 26的array，对应26个字母
        #s 的count +1. t的count -1， 看最后array是不是都是0
        
        if len(s) != len(t):
            return False
        count =  [0]*26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1

        for val in count:
            if val != 0:
                return False
        return True