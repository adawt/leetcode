class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
            """
        left, res, d = -1, 0, {}
        for right, c in enumerate(s):
            if c in d and d[c] > left:
                left = d[c]
            elif right - left > res:
                res = right-left
            d[c] = right
        return res


print(Solution().lengthOfLongestSubstring(s='abcabcabc'))