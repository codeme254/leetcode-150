from typing import Optional
# Solution from neetcode: https://www.youtube.com/watch?v=5Y2EiZST97Y
"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        """
        construct a deep copy of a linked list with random pointers

        Args:
          head: the first node of the list to be cloned
        
        Returns:
          the head node of the cloned list
        """
        oldToCopy = { None: None }
        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        
        return oldToCopy[head]