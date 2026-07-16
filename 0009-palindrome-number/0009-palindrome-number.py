class Solution:
    def isPalindrome(self, x: int) -> bool:
        original=0
        temp=x
        while x>0:
            digits=x%10
            original=original*10 + digits
            x//=10
        if original==temp:
            return True
        else:
            return False
        