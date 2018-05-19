class Solution:
    def twoSum(self, nums, target):
        # for i in range(len(nums)-1):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        a = {}
        for index, item in enumerate(nums):
            if target - item in a:
                return a[target - item], index
            a[item] = index
            # for key, value in a.items():
            #     b = target - key
            #     if b in a and a[b] != value:
            #         return [value, a[b]]


nums = [3, 3]
print(Solution().twoSum(nums, 6))



