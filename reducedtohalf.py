num = 14
class Solution(object):
    def numberOfSteps(self, num):
        self.num = num 
        times = 0
        while num != 0 : 
            # helps use a loop for specific condition - like uptill num = 0 we repeat the loop
            if num%2 == 0 : 
                num = num/2
                times += 1
            else : 
                num -= 1 
                times += 1
        return times
        # methods need to have a definitive return value
sol = Solution()          
times = sol.numberOfSteps(num)     
print(times)
