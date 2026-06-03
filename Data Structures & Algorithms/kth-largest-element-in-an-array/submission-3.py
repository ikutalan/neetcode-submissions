class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k

        def partition(left, right):
            pivot = nums[right]
            wall = left
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[wall], nums[j] = nums[j], nums[wall]
                    wall += 1
            nums[wall], nums[right] = nums[right], nums[wall]
            return wall
        
        left, right = 0, len(nums) - 1
        while left <= right:
            p = partition(left, right)
            if p == target:
                return nums[p]
            elif p < target:
                # go right half
                left = p + 1
            else:
                # go left half
                right = p - 1
        