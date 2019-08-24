# coding=utf-8
print '''
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3
'''

from LinkedList import *


def deleteDuplicates(head):
    if not head: return head
    node = head
    data = set()
    while node and node.next:
        if node.val == node.next.val:
            node.next = node.next.next
            data.add(node.val)
        else:
            node = node.next

    dump = ListNode(None)
    dump.next = head
    node = dump
    while node and node.next:
        if node.next.val in data:
            node.next = node.next.next
        else:
            node = node.next

    return dump.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(3)
l2.next.next.next.next = ListNode(4)
l2.next.next.next.next.next = ListNode(4)
l2.next.next.next.next.next.next = ListNode(5)

foreachListNode(deleteDuplicates(l2))
