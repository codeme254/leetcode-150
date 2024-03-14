from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        detects if a singly linked list has a cycle

        Args:
          head: first node of a singly linked list
        
        Returns:
          true if the list has a cycle and false otherwise
        """
        seen_nodes = {}
        current_node = head
        while current_node:
            if current_node in seen_nodes:
                return True
            seen_nodes[current_node] = True
            current_node = current_node.next
        return False
s = Solution()
print(s.hasCycle([3,2,0,-4]))