# coding=utf-8
print '''
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。

示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
'''

from LinkedList import *


def rotateRight(head, k):
    if not head or k < 1: return head
    node = head
    length = 1
    while node.next:
        length += 1
        node = node.next

    # 循环列表
    node.next = head
    tmp = head
    k = k % length

    for i in range(length - k - 1):
        tmp = tmp.next

    new_head = tmp.next
    tmp.next = None
    return new_head


l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(5)

foreachListNode(rotateRight(l2, 2))
