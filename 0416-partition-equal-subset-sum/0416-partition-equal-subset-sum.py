class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        t=sum(nums)
        if t%2!=0:
            return False
        else:
            s=int(t/2)
            dp=[[-1] * (s+1) for i in range(n)]
            return self.solve(n-1,s,nums,dp)


        
    def solve(self, n,s,arr,dp):
        if s==0:
            return True
        if n==0:
            if arr[0]==s:
                return True
            return False
        
        if dp[n][s]!=-1:
            return dp[n][s]
        notPick=self.solve(n-1,s,arr,dp)
        pick=0
        if arr[n]<=s:
            pick=self.solve(n-1,s-arr[n],arr,dp)
        dp[n][s]=pick or notPick
        return dp[n][s]
        
        