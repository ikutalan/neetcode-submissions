class Solution:
    def findMin(self, nums: List[int]) -> int:
        # nums has a place where the nums are rotated
        # so find the not rotated half, then min = that half + 1
        t = nums[-1]
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi) // 2
            if t >= nums[mid]:
                hi = mid
            else:
                lo = mid + 1
        return nums[lo]