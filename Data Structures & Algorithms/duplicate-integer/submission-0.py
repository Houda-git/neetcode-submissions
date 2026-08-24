class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_duplicate_nums = set(nums)
        return len(nums) != len(non_duplicate_nums)
        