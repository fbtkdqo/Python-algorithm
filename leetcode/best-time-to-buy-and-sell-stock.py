from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize

        #최솟값 최댓값 경신
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)

        return profit