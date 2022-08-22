#Optimized solution

def maxProfit(prices):
        import math
        #Set min price to default value of infinite
        min_price = math.inf
        #Set initial profit at 0 - worst case scenario
        max_profit = 0
        for index in range(len(prices)):
            #Update minimum if lower value is found
            if prices[index] < min_price:
                min_price = prices[index]
            elif prices[index] - min_price > max_profit:
                #Update max_profit if better value is found
                max_profit = prices[index] - min_price
        #Since max_profit is based on the current minimum, even if an unoptimal minimum is found, the previous max_profit will prevail and be the return value
        return max_profit
        
print(maxProfit([1,1,5,0,0,3])) 