class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        largest = 0
        max_profit = 0
        temp_profit = 0
        init = False # Check if there even is a lowest in play
        for x in range(len(prices)):
            # When you pick the lowest you have to wipe the highest
            if prices[x] < cheapest:
                cheapest = prices[x]
                largest = prices[x]
                init = True
            elif prices[x] >= largest and prices[x] > cheapest:
                largest = prices[x]
                temp_profit = largest - cheapest
                # you keep the lowest var here 
            if temp_profit > max_profit:
                    max_profit = temp_profit
        return max_profit