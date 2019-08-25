# coding=utf-8
print '''
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL
'''

from LinkedList import *


def reverseBetween(head, m, n):
    if not head or not head.next or n <= m: return head
    dump = ListNode(None)
    dump.next = head

    # 截取合适子链表
    end_node = dump
    start_node = None
    for i in range(n):
        if i == m - 1:
            start_node = end_node
        end_node = end_node.next

    temp = end_node.next
    end_node.next = None
    # 翻转子链表
    start1, end1 = reverseList(start_node.next)

    # 将原链表与翻转后的链表：拼接在一起
    start_node.next = start1
    end1.next = temp
    return dump.next


l1 = ListNode(1)
l1.next = ListNode(2)
# l1.next.next = ListNode(3)
# l1.next.next.next = ListNode(4)
# l1.next.next.next.next = ListNode(5)

foreachListNode(reverseBetween(l1, 1, 2))
