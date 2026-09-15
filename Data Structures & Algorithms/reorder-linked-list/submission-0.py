# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        cur = head
        nums = []
        while cur:
            nums.append(cur.val)
            cur = cur.next
        cur = head
        for i in range(len(nums)):
            if i%2==0:
                head.val = nums[i//2]
            else:
                head.val = nums[len(nums)-(i//2+1)]

            head = head.next

        