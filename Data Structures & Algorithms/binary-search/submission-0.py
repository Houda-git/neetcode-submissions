class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def binary_search(left, right):
            if right < left:
                return -1
            mid = (left + right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return binary_search(left, right-1)
            else:
                return binary_search(left+1, right)
        return binary_search(0,len(nums)-1)