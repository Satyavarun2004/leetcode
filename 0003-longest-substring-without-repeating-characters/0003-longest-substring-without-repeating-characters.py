class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len=0
        n=len(s)
        for i in range(n):
            hash=[0]*256
            for j in range(i,n):
                if hash[ord(s[j])]==1:
                    break
                lent=j-i+1
                max_len=max(lent,max_len)
                hash[ord(s[j])]=1
        return max_len
        