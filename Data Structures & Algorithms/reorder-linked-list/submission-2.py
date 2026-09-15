# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        prev = slow.next = None

        while second:
            tmp = second.next
            second.next = prev
            prev = second 
            second = tmp

        second = prev

        first,second =  head, prev

        while second:
            tmp1,tmp2 = first.next,second.next
            first.next = second
            second.next = tmp1
            first,second = tmp1, tmp2









        # cur = head
        # nums = []
        # while cur:
        #     nums.append(cur.val)
        #     cur = cur.next
        # l = len(nums)
        # for i in range(l):
        #     if i%2==0:
        #         head.val = nums[i//2]
        #     else:
        #         head.val = nums[l-(i//2+1)]

        #     head = head.next

        