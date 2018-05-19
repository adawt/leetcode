class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if not s:
            return 0
        l = len(s) - 1
        while l >= 0:
            if s[l] != ' ':
                l -= 1
            else:
                break
        return len(s) - 1 - l
