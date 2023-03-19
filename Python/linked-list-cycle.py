# 141. 环形链表
# linked-list-cycle

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        shown = []
        while head:
            if head in shown: return True
            shown.append(head)
            head = head.next
        return False