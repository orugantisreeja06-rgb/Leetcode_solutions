class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low=max(nums)
        high=sum(nums)
        res=0
        if k==1:
            return high
        if k==len(nums):
            return low
        while low <=high:
            mid=low+(high-low)//2
            if self.isPossible(nums,k,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    def isPossible(self,nums,k,mid):
        used=1
        remaining=mid
        for num in nums:
            if remaining>=num:
                remaining-=num
            else:
                used+=1
                remaining=mid
                remaining-=num
        return used<=k

       
        