# coding=utf-8
print '''给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
'''

from LinkedList import *


def reorderList(head):
    if not head or not head.next: return head

    array = []
    node = head
    while node:
        array.append(node)
        node = node.next

    start = 0
    end = len(array) - 1
    result = ListNode(None)
    node = result
    while start <= end:
        node.next = array[start]
        node.next.next = array[end]
        node = node.next.next
        start += 1
        end -= 1
    node.next = None
    return result.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)

foreachListNode(reorderList(l2))
foreachListNode(reorderList(l1))
