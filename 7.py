class Solution:
    def reverse(self, x):
        b = ''
        a = str(x)
        if int(x) < 0:
            a = a[1:]
            b = -int(a[::-1])
        if int(x) > 0:
            b = int(a[::-1])
        if -2 ** 31 < b < 2 ** 31 - 1:
            return b
        else:
            return 0


print(Solution().reverse(76854391))

