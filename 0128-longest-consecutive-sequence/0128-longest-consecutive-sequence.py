class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dict1=set(nums)
        longest=0
        for num in dict1:
            if num-1 not in dict1:
                curr=num
                length=1
                while curr+1 in dict1:
                    curr=curr+1
                    length+=1
                longest=max(longest,length)
        return longest
            
