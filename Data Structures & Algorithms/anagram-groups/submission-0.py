class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for string in strs:
            count = [0] * 26

            for c in string:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(string)

        return list(anagrams.values())

            
