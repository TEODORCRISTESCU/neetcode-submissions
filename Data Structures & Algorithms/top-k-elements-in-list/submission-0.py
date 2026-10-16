class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        seen_freq = {}
        for num in nums:
            if num not in seen_freq:
                seen_freq[num] = 1

            else:
                seen_freq[num] += 1

        sorted_keys = sorted(seen_freq, key=seen_freq.get, reverse = True)

        return sorted_keys[:k]