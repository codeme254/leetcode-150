from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        Removes the nth node from the end of a list

        Args:
          head: first node of the input list
          n: index of the node to be removed from the end

        Returns:
          the head of the modified list
        """
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        if length == 1:
            return None
        
        if n == length:
            current_head = head
            head = current_head.next
            current_head.next = None
            return head
        
        current = head
        previous = head
        while current:
            if length == n:
                previous.next = current.next
                current.next = None
                break
            length -= 1
            previous = current
            current = current.next
        return head

        