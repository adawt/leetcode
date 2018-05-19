# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeTwolists(self, l1, l2):
        new_list = ListNode(0)
        pre = new_list
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                pre.next = l1
                l1 = l1.next
            else:
                pre.next = l2
                l2 = l2.next
            pre = pre.next
        if l1 is not None:
            pre.next = l1
        else:
            pre.next = l2
        return new_list.next


l1 = ListNode(1)
l1.next = ListNode(2)
l2 = ListNode(1)
l2.next = ListNode(3)

d = Solution().mergeTwolists(l1, l2)
while d is not None:
    print(d.val)
    d = d.next

