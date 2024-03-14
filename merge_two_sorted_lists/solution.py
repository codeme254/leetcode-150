from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Merges two linked lists sorted in ascending order into one

        Args:
          list1: first linked list sorted in ascending order
          list2: second linked list sorted in ascending order
        
        Returns:
          One list that is sorted in ascending order
        """
        temp_list = ListNode()
        append_position = temp_list
        if not list1 and not list2:
            return list1
        
        current_l1 = list1
        current_l2 = list2

        while current_l1 and current_l2:
            if current_l1.val <= current_l2.val:
                append_position.next = current_l1
                current_l1 = current_l1.next
            else:
                append_position.next = current_l2
                current_l2 = current_l2.next
            append_position = append_position.next
        
        while current_l1:
            append_position.next = current_l1
            current_l1 = current_l1.next
            append_position = append_position.next
        
        while current_l2:
            append_position.next = current_l2
            current_l2 = current_l2.next
            append_position = append_position.next
        return temp_list.next
        