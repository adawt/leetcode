class Solution:
    def removeDuplicates(self, nums):
        if len(nums) == 0:
            return 0
        temp = nums[0]
        index = 1
        while index != len(nums):
            if nums[index] == temp:
                nums.pop(index)
            else:
                temp = nums[index]
                index += 1
        return index


print(Solution().removeDuplicates(nums=[1, 2, 2, 3, 5]))
