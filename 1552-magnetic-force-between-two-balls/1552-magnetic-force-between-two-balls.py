class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        n=len(position)
        l=1
        r=position[n-1]-position[0]
        res=1
        while l<=r:
            mid=l+(r-l)//2
            if self.check(position,mid,m):
                res=mid
                l=mid+1
            else:
                r=mid-1
        return res
    def check(self,position,mid,k):
        n=len(position)
        count=1
        last=position[0]
        for i in range(1,n):
            if position[i]-last>=mid:
                count+=1
                last=position[i]
        return count>=k
        
        