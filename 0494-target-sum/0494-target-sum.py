class Solution:
    def solve(self,index,nums,target):
        if index==0:
            if nums[0]==0 and target==0:
                return 2
            if nums[0]==target:
                return 1
            if target==0:
                return 1
            return 0


        NotPick=self.solve(index-1,nums,target)
        pick=0
        if nums[index]<=target:
            pick=self.solve(index-1,nums,target-nums[index])
      
        return pick+NotPick
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        sum1=sum(nums)
        if (sum1-target)%2==1:
            return 0
        if target>sum1 or target<-sum1:
            return 0
        return self.solve(n-1,nums,(sum1-target)//2)
        