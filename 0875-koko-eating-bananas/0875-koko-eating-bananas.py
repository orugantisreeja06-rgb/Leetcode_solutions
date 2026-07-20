class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low=1
        high=max(piles)
        res=0
        while low<=high:
            mid=low+(high-low)//2
            if self.check(piles,h,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    def check(self,piles,h,mid):
        count=0
        for i in piles:
            count=count+ceil(i/mid)
        return count<=h
     


        