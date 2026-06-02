class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        n = len(prices)
        maximum_profit = 0
        while right < n:
            profit = prices[right] - prices[left]
            if profit <= 0:
                left = right
                right += 1
            else:
                right += 1
            maximum_profit = max(maximum_profit, profit)
        return maximum_profit
        