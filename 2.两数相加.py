#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import List


class Solution:
    def ListNode_to_List(self, listnode: ListNode) -> List:
        lists = []
        lists.append(listnode.val)
        listnode_next = listnode.next
        while listnode_next:
            lists.append(listnode_next.val)
            listnode_next = listnode_next.next
        return lists
    def List_to_ListNode(self, lists: List) -> ListNode:
        lists = lists[::-1]
        list_node = ListNode(val=lists[0], next=None)
        for i in range(1, len(lists)):
            list_node = ListNode(val=lists[i], next=list_node)
        return list_node


    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1_lists = self.ListNode_to_List(l1)
        l2_lists = self.ListNode_to_List(l2)
        l1_vaule = sum([v * 10 ** i for i, v in enumerate(l1_lists)])
        l2_value = sum([v * 10 ** i for i, v in enumerate(l2_lists)])
        sum_value = l1_vaule + l2_value
        result_lists = [int(v) for v in list(str(sum_value)[::-1])]
        return self.List_to_ListNode(result_lists)
# @lc code=end

solution = Solution()
print(solution.addTwoNumbers([2,4,3], [5,6,4]))