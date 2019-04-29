#!/usr/bin/env python 
# encoding: utf-8 

"""
@author: zkjiang
@description:经典题目，反转链表
@time: 2019/4/29 13:02
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = None
        next = None
        while head:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
