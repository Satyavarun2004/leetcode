class Solution:
    def firstUniqChar(self, s: str) -> int:
        c={}
        for ch in s:
            if ch not in c:
                c[ch]=1
            else:
                c[ch]+=1
        for i,ch in enumerate(s):
            if c[ch]==1:
                return i
        return -1
        