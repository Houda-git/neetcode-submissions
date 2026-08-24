class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # another approach that is less in complexity
        difference_map ={}
        for i in range(len(nums)):
           difference = target - nums[i]
           if difference in difference_map:
            return [difference_map[difference],i]
           difference_map[nums[i]] = i

        