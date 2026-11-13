class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prodLeft = {}
        prod = 1

        for i in range(len(nums)):
            prodLeft[i] = prod
            prod *= nums[i]

        prodRight = {}
        prod = 1

        for i in range(len(nums) - 1, -1, -1):
            prodRight[i] = prod
            prod *= nums[i]

        return [prodLeft[i] * prodRight[i] for i in range(len(nums))]