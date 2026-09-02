class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        minCost = [0] * len(cost)
        minCost[len(cost) - 1] = cost[len(cost) - 1]
        minCost[len(cost) - 2] = cost[len(cost) - 2]
        index=  len(cost) - 3
        while index >= 0:
            minCost[index] = cost[index] + min(minCost[index + 1], minCost[index + 2])
            index -= 1
        return min(minCost[0], minCost[1])


        

        