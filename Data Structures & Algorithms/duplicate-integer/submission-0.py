class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # 解法： 遍历整个array，如果不存在set里，把num加到set里，否则return false
        seen = set()
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
