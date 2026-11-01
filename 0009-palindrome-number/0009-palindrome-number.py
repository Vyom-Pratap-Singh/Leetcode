class Solution(object):
    def isPalindrome(self, x):
        n=x
        r=0
        while x>0:
            d=x%10
            r=(10*r)+d
            x=x//10
        if n==r:
            return True
        else:
            return False

        

        