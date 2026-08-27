from math import comb
class Solution:
    def climbStairs(self, n: int) -> int:
        result = 0 
        for i in range(n//2 + 1):
            result += comb(n-i, i)
        return result