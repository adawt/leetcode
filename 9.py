class Solution:
    def isPalindrome(self, x):
        a = str(x)
        n = len(a)
        for i in range(0, n):
            if a[i] != a[n - 1 - i]:
                return False
        else:
            return True


print(Solution().isPalindrome(1000021))

