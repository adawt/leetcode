class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        last = self.countAndSay(n-1)
        ln, res, count = last[0], '', 0
        for i in last:
            if i != ln:
                res += str(count) + ln
                count = 0
            else:
                count += 1
                ln = i
        res += str(count) + ln
        return res
