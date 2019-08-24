# coding=utf-8

print '''反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL'''

from LinkedList import *


def reverseList(head):
    if not head or not head.next: return head
    dump = ListNode(0)
    dump.next = head

    new_head = ListNode(None)
    while dump and dump.next:
        t = dump.next
        dump.next = dump.next.next
        t2 = new_head.next
        new_head.next = t
        t.next = t2

    return new_head.next


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)

foreachListNode(l2)
print "反："
foreachListNode(reverseList(l2))
