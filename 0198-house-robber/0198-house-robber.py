class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[-1] * (n+1)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        return self.ways(n,nums,dp)
    def ways(self,n,nums,dp):
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        if dp[n]!=-1:
            return dp[n]
        dp[n]=max(nums[n-1]+self.ways(n-2,nums,dp),self.ways(n-1,nums,dp))
        return dp[n]

        
    

        