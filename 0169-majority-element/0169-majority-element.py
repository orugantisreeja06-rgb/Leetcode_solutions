class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dict1={}
        for i in range(len(nums)):
            if nums[i] not in dict1:
                dict1[nums[i]]=1
            else:
                dict1[nums[i]]+=1
        for i,c in dict1.items():
            if c>len(nums)//2:
                return i