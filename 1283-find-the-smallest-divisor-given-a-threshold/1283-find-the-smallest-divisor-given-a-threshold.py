class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        low=1
        high=max(nums)
        res=0
        while low<=high:
            mid=low+(high-low)//2
            if self.check(nums,threshold,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    def check(self,nums,threshold,mid):
        count=0
        for i in nums:
            count=count+ceil(i/mid)
        return count<=threshold

        