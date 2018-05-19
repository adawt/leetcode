class Solution:
    def romanToInt(self, s):
        sum1 = 0
        convert = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        for i in range(len(s) - 1):
            # if (s[i]=='I' or s[i]=='X' or s[i]=='C') and convert[s[i]]<convert[s[i+1]]:
            if convert[s[i]] < convert[s[i + 1]]:
                sum1 = sum1 - convert[s[i]]
            else:
                sum1 = sum1 + convert[s[i]]
        return sum1 + convert[s[-1]]