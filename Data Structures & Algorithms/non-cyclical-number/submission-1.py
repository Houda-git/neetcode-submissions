class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_digits(n):
            count = 0
            while n != 0:
                count += (n%10)**2
                n = n//10
            return count
        counts =set()
        while sum_digits(n) != 1:
            result = sum_digits(n)
            if result in counts: 
                return False
            counts.add(result)
            n = sum_digits(result)
        return True
            
            



        