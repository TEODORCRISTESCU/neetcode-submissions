class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for string in strs:
            temp = {}
            for c in string:
                if c not in temp:
                    temp[c] = 1
                else:
                    temp[c] += 1
            
            key = tuple(sorted(temp.items()))
            
            if key not in anagrams:
                anagrams[key] = []
            anagrams[key].append(string)
            
        return list(anagrams.values())