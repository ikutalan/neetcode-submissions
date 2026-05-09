class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #   1,2,4,6
        #r: 1,1,2,8
        #l: 48,24,6,1

        
        l = len(nums)
        right, left = [1]*l, [1]*l
        for i in range(l):
            if i == 0:
                continue
            right[i] = right[i-1]*nums[i-1]
        
        for i in range(l-1, -1, -1):
            if i == l-1:
                continue
            left[i] = (left[i+1]*nums[i+1])

        res = []
        for i in range(l):
            res.append(right[i]*left[i])
        return res