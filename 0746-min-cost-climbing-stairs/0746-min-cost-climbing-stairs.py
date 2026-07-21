class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        dp=[-1] * n
        return min(self.ways(n-1,cost,dp),self.ways(n-2,cost,dp))
    def ways(self,n,cost,dp):
        if n<=1:
            return cost[n]
        if dp[n]!=-1:
            return dp[n]
        dp[n]=cost[n]+min(self.ways(n-1,cost,dp),self.ways(n-2,cost,dp))
        return dp[n]
         
        