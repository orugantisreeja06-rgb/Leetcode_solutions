class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        dict1={}
        for i in range(len(s)):
            if s[i] not in dict1:
                dict1[s[i]]=1
            else:
                dict1[s[i]]+=1
        for i in range(len(t)):
            if t[i]  not in dict1:
                return False
            else:
                dict1[t[i]]-=1
                if dict1[t[i]]==0:
                    del dict1[t[i]]
        return len(dict1)==0

        