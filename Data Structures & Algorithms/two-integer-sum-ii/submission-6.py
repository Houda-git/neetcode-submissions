class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)
        for i in range(len(numbers)):
            diff = target - numbers[i]
            if mp[diff]:
                # vu que je l'ai deja dans le dictionnaire donc son index est inferieur à i+1
                return [mp[diff], i+1]
            mp[numbers[i]] = i+1
        return []
        