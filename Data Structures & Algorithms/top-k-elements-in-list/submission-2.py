class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # get the count for each num
        # bucket sort，put the same count num into the same bucket(array)
        # find the top K element in the bucket and return
        freq = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for n, count in freq.items():
            bucket[count].append(n)
        
        res = []
        for i in range(len(bucket) - 1, 0, -1): # from right most
            for n in bucket[i]:
                res.append(n)
                if len(res) == k:
                    return res