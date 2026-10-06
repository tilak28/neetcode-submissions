class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0 # left - Buy 
        j = 1 # right = sell

        while j < len(prices):
            #profitable?
            if prices[i] < prices[j]:
                max_profit = max(max_profit, prices[j] - prices[i])
            else:
                i = j
            j += 1
        
        return max_profit