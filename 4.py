class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums.sort()
        l = len(nums)
        d = l//2
        if len(nums) % 2 == 1:
            return nums[d]
        return (nums[d-1] + nums[d]) / 2


print(Solution().findMedianSortedArrays(nums1=[1,3],nums2=[2]))