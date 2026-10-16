class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for string in strs:
            count = [0] * 26

            for c in string:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count) ### for an array like count with 25 elements, if element 
                               # 1 3 and 5 appear, the tuple will make it (1, 0, 1, 0 , 1, 0, ... 0), which will be unique for each anagram

            if key not in anagrams:
                anagrams[key] = []

            anagrams[key].append(string)

        return list(anagrams.values())

            
