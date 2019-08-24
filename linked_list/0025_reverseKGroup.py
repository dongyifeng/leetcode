# coding=utf-8

print '''
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

示例 :

给定这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

说明 :

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换
'''

from LinkedList import *


def reverseList(head):
    if not head or not head.next: return head
    dump = ListNode(0)
    dump.next = head

    new_head = ListNode(None)
    tail = head
    while dump and dump.next:
        t = dump.next
        dump.next = dump.next.next
        t2 = new_head.next
        new_head.next = t
        t.next = t2
    return (new_head.next, tail)


def reverseKGroup(head, k):
    if not head or not head.next or k < 2: return head
    dump = ListNode(0)
    dump.next = head

    s = dump
    while s:
        end = s
        for i in range(k):
            end = end.next
            if not end: return dump.next
        t = end.next
        end.next = None
        new_head, new_tail = reverseList(s.next)

        # 拼接
        s.next = new_head
        new_tail.next = t
        s = new_tail
    return dump.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)

# head, tail = reverseList(l2)

# print tail.val

# foreachListNode(head)
foreachListNode(reverseKGroup(l2, 1))
# foreachListNode(reverseList(l2)),
