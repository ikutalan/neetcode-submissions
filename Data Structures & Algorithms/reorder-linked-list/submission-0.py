# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        slow.next = None

        # reverse the second half
        cur = second_half
        pre = None

        while cur:
            temp = cur.next
            cur.next = pre
            pre = cur
            cur = temp
        
        # merge two list
        l1 = head
        l2 = pre
        dummy = ListNode()
        tail = dummy
        while l1 and l2:
            temp1 = l1.next
            temp2 = l2.next
            #merge
            l1.next = l2
            l2.next = temp1
            #both move to the next
            l1 = temp1 
            l2 = temp2 