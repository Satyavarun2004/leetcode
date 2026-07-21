class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        l=[]
        while n>0:
            bit=n%2
            l.insert(0,bit)
            n=n//2
        for i in range(len(l)-1):
            if l[i]==l[i+1]:
                return False
        return True
