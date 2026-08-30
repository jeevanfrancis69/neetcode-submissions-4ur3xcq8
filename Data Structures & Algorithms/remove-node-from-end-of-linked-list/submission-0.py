# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #traverse the fast pointer first
        fast = head
        for count in range(n):
            fast = fast.next

        slow = head
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        while (fast is not None):
            #traverse until fast reaches null pointer so to get nth node from last
            fast = fast.next
            prev = slow
            slow = slow.next


        nextN = slow.next
        prev.next = nextN
        return dummy.next
          


        