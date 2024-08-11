# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        first = head

        # find the middle of the list 
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # slow.next is the beginning of the second half of the list
        second = slow.next
        slow.next = None

        prev = None
        while second:
            next_node = second.next
            second.next = prev
            prev = second
            second = next_node
        second = prev

        # merge the tho linked lists (first and second)
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1
            first = temp1
            second = temp2    

        