class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        somme = 0
        somme_nums = 0
        for num in range(n+1):
            somme += num
        for num_ in nums:
            somme_nums += num_
        return somme - somme_nums
        
        