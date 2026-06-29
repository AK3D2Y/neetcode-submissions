class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS,countT = {},{}
        for i,n in zip(s,t):
            countS[i] = 1 + countS.get(i, 0)
            countT[n] = 1 + countT.get(n, 0)    
        return countS == countT