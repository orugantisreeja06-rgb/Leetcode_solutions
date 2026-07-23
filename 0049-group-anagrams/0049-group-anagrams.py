class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1={}
        for i in strs:
            if "".join(sorted(i)) in dict1:
                dict1["".join(sorted(i))].append(i)
            else:
                dict1["".join(sorted(i))]=[i]
        return list(dict1.values())
            
        