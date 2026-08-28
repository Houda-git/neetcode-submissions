class Solution:
    def isHappy(self, n: int) -> bool:
        def sum_digits(n):
            count = 0
            while n != 0:
                count += (n%10)**2
                n = n//10
            return count
        counts =set()
        n = sum_digits(n)
        while n != 1:
            if n in counts: 
                return False
            counts.add(n)
            n = sum_digits(n)
        return True
            
            



        