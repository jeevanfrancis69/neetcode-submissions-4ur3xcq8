# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #separate case for empty lists
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        curr1 = list1
        curr2 = list2
        
        dummyNode = ListNode()
        tail = dummyNode

        while (curr1 is not None and curr2 is not None):
            if (curr1.val >= curr2.val):
                tail.next = curr2
                curr2 = curr2.next
            else:
                tail.next = curr1
                curr1 = curr1.next
            
            tail = tail.next
        
        tail.next = curr1 if curr1 is not None else curr2

        return dummyNode.next


        

            

        