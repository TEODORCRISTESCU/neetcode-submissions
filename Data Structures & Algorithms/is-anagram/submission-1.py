class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        appear1 = {}
        appear2 = {}

        for c in s:
            if c not in appear1:
                appear1[c] = 1

            else:
                appear1[c] += 1

        for c in t:
            if c not in appear2:
                appear2[c] = 1

            else:
                appear2[c] += 1

        return appear1 == appear2