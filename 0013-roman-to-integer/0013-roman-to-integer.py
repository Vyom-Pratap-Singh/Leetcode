class Solution(object):
    def romanToInt(self,s):
        D=0
        Val={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        for i in range(0,len(s)):
            a=s[i]
            if i+1<len(s):
                b=s[i+1]
 
                if Val[b]>Val[a]:
                    D=D-Val[a]
                else:
                    D=D+Val[a]
            else:
                D=D+Val[a]
        return D

        
        