class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # while i < len(nums)
        # num[j] + nums[k] = 0 - nums[i] (target)
        # use 2 sum to find j and k, then return num[i], num[j], num[k]
        nums.sort()
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i-1]:
                i += 1
                continue
            target = - nums[i]
            l,r = i + 1, len(nums) - 1

            while l < r:
                s = nums[l] + nums[r]
                if s == target:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l+=1
                    r-=1
                elif s < target:
                    l += 1
                else:
                    r -= 1
        return res


