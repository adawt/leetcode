class Solution:
    def isValid(self, s):
        if len(s) <= 1:
            return False
        a = list(s)
        b = []
        c = {'(': ')', '{': '}', '[': ']'}
        for i in a:
            if i in c:
                b.append(i)
            else:
                if len(b) == 0:
                    return False
                else:
                    if c.get(b[-1]) != i:
                        return False
                    else:
                        del b[-1]
        if len(b) != 0:
            return False
        return True


print(Solution().isValid('()[]{'))
