class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = defaultdict(int)
        for num in nums:
            map_[num]+=1
        return sorted(
            map_.keys(), 
            key= lambda x: map_[x],
            reverse=True)[:k]
        