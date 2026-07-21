class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        curr=[]
        visited=[False] * len(nums)
        self.backtrack(0,nums,visited,curr,res)
        return res
    def backtrack(self,index,nums,visited,curr,res):
        if len(curr)==len(nums):
            res.append(curr.copy())
            return
        if index>=len(nums):
            return 
        for i in range(len(nums)):
            if visited[i]:
                continue
            curr.append(nums[i])
            visited[i]=True
            self.backtrack(index+1,nums,visited,curr,res)
            visited[i]=False
      
            curr.pop()

        