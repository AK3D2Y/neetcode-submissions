class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS,countT = {},{}
        for i,n in enumerate(s):
            countS[n] = 1 + countS.get(n, 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)    
        return countS == countT