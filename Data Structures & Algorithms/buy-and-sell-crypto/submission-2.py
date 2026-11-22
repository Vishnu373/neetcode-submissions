class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Profit - buy low, sell high. 
        - Thus, you only need to calculate profit when your buying price is less than selling price.
        - Secondly, you can only buy until the last day.

        - buying_day = 0
        - selling_day


        """

        buying_day = 0
        selling_day = 1
        max_profit = 0

        while selling_day < len(prices):
            if prices[buying_day] < prices[selling_day]:
                profit = prices[selling_day] - prices[buying_day]
                max_profit = max(max_profit, profit)

            else:
                buying_day = selling_day
            
            selling_day += 1

        
        return max_profit

