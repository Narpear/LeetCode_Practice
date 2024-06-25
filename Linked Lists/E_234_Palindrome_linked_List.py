# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head

        # slow pointer is the 'middle' of the list after this loop
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # from the slow pointer till the fast(end) pointer, reverse the list.
        prev = None
        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next

        # check from head side and from tail side. (since the second half of the list is reversed, head.next would point in the backward direction)
        left, right = head, prev

        # the middle of the list is a None pointer (because the first prev is None)
        while right:
            if left.val!=right.val:
                return False
            left = left.next
            right = right.next
        
        return True