class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        running = 1
        for i in range(len(nums)):
            prefix[i] = running
            running *= nums[i]

        suffix = [1] * len(nums)
        running = 1
        for i in range(len(nums) -1, -1, -1):
            suffix[i] = running
            running *= nums[i]

        res = []
        for i in range(len(nums)):
            res.append(prefix[i] * suffix[i])

        return res