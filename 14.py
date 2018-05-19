class Solution:
    def longgestCommonPrefix(self, strs):
        common = ''
        for _ in zip(*strs):
            if len(set(_)) != 1:
                break
            common += _[0]
        return common


strs = ["flower","flow","flight"]
print(Solution().longgestCommonPrefix(strs))