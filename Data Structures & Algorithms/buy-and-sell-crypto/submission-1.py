class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buying, selling = 0, 0
        max_profit = 0

        while selling < len(prices):
            if prices[buying] < prices[selling]:
                profit = prices[selling] - prices[buying]
                max_profit = max(max_profit, profit)
            
            else:
                buying = selling

            selling += 1

        return max_profit
        