class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        res = 0
        counter = 0
        for i in range(len(nums)):
            if i == 0:
                counter = 1
            elif nums[i] == nums[i-1]:
                continue
            elif nums[i] == nums[i-1] + 1:
                counter += 1
            else:
                res = max(res,counter)
                counter = 1
        return max(res,counter)
        # sort, de dup - set (?)
        # use a counter, for each element in the list, 
        #if it's +1 of the prev, counter++, if same, skip, else save the max, reset counter
