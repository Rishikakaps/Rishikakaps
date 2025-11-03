# 1672. Richest Customer Wealth
class Solution(object):
    def maximumWealth(self, accounts):
        wealth_sofar = 0 
        for customer in accounts: 
            customer_wealth = 0 
            for bank in customer: 
                customer_wealth += bank
            wealth_sofar = max(wealth_sofar, customer_wealth)
            return wealth_sofar
           

# 1. def class
# 2. def method for class 
# 3. def initial variable 
# 4. loop for checking each customer in matrix 
# 5. adds each bank val for each customer to wealth so far
# 6. compares the wealth so far w new customer wealth 
# 7. whichever is larger becomes wealth so far 

accounts = [[1,5,6] , [4,3,8] , [3,1,9]]
# 12 , 15 , 13 = predicted val = 15

solution = Solution()
print(solution.maximumWealth(accounts))