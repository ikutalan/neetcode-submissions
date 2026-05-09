class Solution:

# how do we know one word ends, and start a new word
# 如果只用一个简单分隔符，不能work，因为有可能在单词里出现
# 所以知道有几个单词，每个单词有几个字母
# 字母数 + 分隔符 + 单词
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + ":" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i<len(s):
            j = i
            while s[j] != ":":
                j += 1
            count = int(s[i:j])
            i = j+1 # word start 
            j = i + count # word end
            res.append(s[i:j])
            i = j # look for the next word
        return res
