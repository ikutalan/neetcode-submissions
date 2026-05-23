class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find out which half is the sorted one
        # then find the target with the sorted half or the not sorted half

        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2
            if target == nums[mid]:
                return mid
            if nums[lo] <= nums[mid]:
                # sorted half is lo ~ mid
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1
                else: 
                    lo = mid + 1
            else: # sorted hal is mid ~ hi
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1
                else: 
                    hi = mid - 1
        return -1