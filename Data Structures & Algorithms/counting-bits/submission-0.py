class Solution:
    def countBits(self, n: int) -> List[int]:
        bits = []
        for i in range(n+1):
            bits.append(bin(i).count('1'))
        return bits
        