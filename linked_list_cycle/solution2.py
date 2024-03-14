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
        runner = head
        walker = head

        while runner and runner.next:
            walker = walker.next
            runner = runner.next.next
            if runner == walker:
                return True
        return False
s = Solution()
print(s.hasCycle([3,2,0,-4]))