from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        adds two numbers represented by two non-empty linked lists stored in reverse order

        Args:
          l1: the first list representing the first number in reversed format
          l2: the second list representing the second number in reversed format
        
        Returns:
          the sum of the two numbers represented as a linked list
        """
        result = ListNode(0)
        current_append = result
        current_l1 = l1
        current_l2 = l2
        carry = 0
        while (current_l1) or (current_l2):
            current_summation = 0
            left_operand = 0
            right_operand = 0
            if current_l1 != None:
                left_operand = current_l1.val
            if current_l2 != None:
                right_operand = current_l2.val
            current_summation = left_operand + right_operand + carry
            carry = 0
            current_val_for_new_node = 0
            if current_summation >= 10:
                current_val_for_new_node = current_summation % 10
                carry = current_summation // 10
            else:
                current_val_for_new_node = current_summation
            new_node = ListNode(current_val_for_new_node)
            current_append.next = new_node
            current_append = new_node

            if current_l1 != None:
                current_l1 = current_l1.next
            if current_l2 != None:
                current_l2 = current_l2.next
        if carry > 0:
            new_node = ListNode(carry)
            current_append.next = new_node
        return result.next
