class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        res=0
        while low<=high:
            mid=low+(high-low)//2
            if self.isPossible(weights,days,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    def isPossible(self,weights,days,mid):
        days_used=1
        remaining=mid
        
        for weight in weights:
            if remaining>=weight:
                remaining-=weight
            else:
                days_used+=1
                remaining=mid
                remaining-=weight
                

        return days_used<=days



      
        
     


        
        