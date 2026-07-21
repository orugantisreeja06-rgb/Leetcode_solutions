class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        self.backtrack(0,nums,curr,res)
        return res
    def backtrack(self,index,nums,curr,res):
        res.append(curr.copy())
        if index>=len(nums):
            return
        for i in range(index,len(nums)):
            curr.append(nums[i])
            self.backtrack(i+1,nums,curr,res)
            curr.pop()

     
        