class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        appearance = {}

        for num in nums:
            if num not in appearance:
                appearance[num] = 1
            else:
                appearance[num] += 1

        sorted_items = sorted(appearance.items(), key=lambda item: item[1], reverse=True)

        res = []

        for item in sorted_items[:k]:
            res.append(item[0])

        return res