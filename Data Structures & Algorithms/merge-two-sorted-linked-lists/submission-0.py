# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next,list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1,list2.next)
            return list2




        # list3 = ListNode()
        # if list1 and not list2:
        #     list3 = list1
        # elif not list1 and list2:
        #     list3 = list2
        # elif not list and not list2:
        #     return []
        # elif list1.val <= list2.val:
        #     list3 = list1
        #     list1 = list1.next
        # else:
        #     list3 = list2
        #     list2 = list2.next

        # while list1 or list2:
        #     if list1 and not list2:
        #         list3.next = list1
        #         list1 = list1.next
        #     elif list2 and not list1:
        #         list3.next = list2
        #         list2 = list2.next
        #     elif list1.val < list2.val:
        #         list3.next = list1
        #         list1 = list1.next
        #     elif list2.val < list1.val:
        #         list3.next = list2
        #         list2 = list2.next
        #     else:
        #         list3.next = list1
        #         list3 = list3.next
        #         list3.next = list2
        #     list3= list3.next

        # return list3

            

        