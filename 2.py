# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = ListNode(0)
        pre = new_list
        flag = 0
        while l1 is not None and l2 is not None:
            sum1 = l1.val + l2.val + flag
            flag = int(sum1/10)
            pre.next = ListNode(sum1 % 10)
            pre = pre.next
            l1 = l1.next
            l2 = l2.next
        if l1 is None:
            l1 = l2
        while l1 is not None:
            sum1 = l1.val + flag
            flag = int(sum1/10)
            pre.next = ListNode(sum1 % 10)
            pre = pre.next
            l1 = l1.next
        if flag != 0:
            pre.next = ListNode(flag)
            pre = pre.next
        pre.next = None
        return new_list.next


l1 = ListNode(1)
l1.next = ListNode(2)
l2 = ListNode(9)
l2.next = ListNode(3)

d = Solution().addTwoNumbers(l1, l2)
while d is not None:
    print(d.val)
    d = d.next




