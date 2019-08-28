# coding=utf-8
print '''
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶:

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

示例:

输入: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出: 7 -> 8 -> 0 -> 7
'''

from LinkedList import *
from stack.Stack import Stack


def addTwoNumbers(l1, l2):
    l1_node = l1
    stack1 = Stack()
    while l1_node:
        stack1.push(l1_node.val)
        l1_node = l1_node.next

    l2_node = l2
    stack2 = Stack()
    while l2_node:
        stack2.push(l2_node.val)
        l2_node = l2_node.next

    result = ListNode(None)
    s = 0
    while stack1.size() > 0 and stack2.size() > 0:
        num1 = stack1.pop()
        num2 = stack2.pop()

        node = ListNode(((num1 + num2 + s) % 10))
        node.next = result.next
        result.next = node
        s = int((num1 + num2 + s) / 10)

    stack = stack1 if stack1.size() > 0 else stack2
    while stack.size() > 0:
        num = stack.pop()
        node = ListNode(((num + s) % 10))
        node.next = result.next
        result.next = node
        s = int((num + s) / 10)
    if s > 0:
        node = ListNode(s)
        node.next = result.next
        result.next = node

    return result.next


l1 = ListNode(7)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l1.next.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

foreachListNode(addTwoNumbers(l1, l2))
