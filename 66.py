class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)-1
        while l >= 0:
            if digits[l] == 9:
                digits[l] = 0
            else:
                digits[l] += 1
                break
            l -= 1
        else:
            digits[0] = 1
            digits.append(0)
        return digits