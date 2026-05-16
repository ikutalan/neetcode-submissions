class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # DP - only maintain the lowest price and the max diff
        min_price = float('inf')
        res = 0
        for price in prices:
            min_price = min(min_price, price)
            res = max(res,price - min_price)
        return res