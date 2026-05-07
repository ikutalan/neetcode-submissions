class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # use hashmap -> num, count
        # ? top k count? res = [0]*k, if curr count > any item in res, replace

        freq = Counter(nums)
        return sorted(freq, key=lambda x: freq[x], reverse=True)[:k]