class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        count = 0
        for num in binary[2:]:
            count+= int(num)
        return count
        