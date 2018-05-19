class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        n = numRows+numRows -2
        d = ['']*numRows
        # for x in range(numRows):
        for index, c in enumerate(s):
            carry = index % n
            if carry < numRows:
                d[carry] += c
            else:
                d[n - carry] += c
        return ''.join(d)


print(Solution().convert(s='PAYPALISHIRING', numRows=3))

