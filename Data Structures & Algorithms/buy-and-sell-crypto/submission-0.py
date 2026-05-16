class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # return max profit
        # max (price[1...i] - price[0...j]) where i > j

        # brute force: for each element i in the array, i get the diff for the elements from [i...n-1]
        # return the max diff

        # two pointer, l = 0, r = 1
        n = len(prices)
        l = 0
        r = 1
        res = 0
        while l < n and r < n:
            if prices[r] > prices[l]:
                res = max(res, (prices[r]-prices[l]))
                r += 1
            else: # 因为以后任何卖出，从这个更低点买入都不会更差
                l = r 
                r += 1
        return res