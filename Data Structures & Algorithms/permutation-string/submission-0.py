class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        count = {}

        for c in s1:
            count[c] = count.get(c, 0) + 1
        
        window = {}

        left = 0

        for right in range(len(s2)):
            if s2[right] in window:
                window[s2[right]] += 1
            else:
                window[s2[right]] = 1

            if right - left + 1 > len(s1):
                if window[s2[left]] > 1:
                    window[s2[left]] -= 1
                
                else:
                    del window[s2[left]]
                left +=1
            
            if right - left + 1 == len(s1):
                if count == window:
                    return True 

        return False


        