# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashCountNode = {}
        
        while (head is not None):
            nextNode = head.next
            hashCountNode[nextNode] = hashCountNode.get(nextNode, 0) + 1
            #check if  it has been visited before

            if (hashCountNode[nextNode] == 2):
                return True
            
            head = nextNode
        
        return False
            

        