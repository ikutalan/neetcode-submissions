class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #brute force
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []
        
        # use hash map
        # diff = targe - curr, find diff's index in the array

        pair = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in pair:
                return [pair[diff],i]
            pair[n] = i
        return []
