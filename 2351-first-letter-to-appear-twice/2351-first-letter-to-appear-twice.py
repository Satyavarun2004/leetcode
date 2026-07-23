class Solution:
    def repeatedCharacter(self, s: str) -> str:
        c={}
        for ch in s:
            if ch not in c:
                c[ch]=1
            else:
                c[ch]+=1
            if c[ch]==2:
                return ch

        