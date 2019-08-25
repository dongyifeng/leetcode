# coding=utf-8
print '''
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5
'''

from LinkedList import *

'''
归并排序：O(n log_n)
'''


def mergeTwoLists(l1, l2):
    node = head = ListNode(0)
    while l1 and l2:
        if l1.val <= l2.val:
            node.next = l1
            l1 = l1.next
        elif l1.val >= l2.val:
            node.next = l2
            l2 = l2.next
        node = node.next

    # 对于非空的链表，拼接到 node 后边
    if l1:
        node.next = l1
    if l2:
        node.next = l2
    return head.next


def sortList(head):
    if not head or not head.next: return head
    fast = slow = head

    pre = None
    while fast and fast.next:
        fast = fast.next.next
        pre = slow
        slow = slow.next
    if not pre:
        return head

    pre.next = None
    # 划分
    right = sortList(slow)
    left = sortList(head)

    # 合并
    return mergeTwoLists(right, left)


l1 = ListNode(4)
l1.next = ListNode(2)
l1.next.next = ListNode(1)
l1.next.next.next = ListNode(3)
l1.next.next.next.next = ListNode(5)
foreachListNode(sortList(l1))

l2 = ListNode(3)
l3 = ListNode(1)
l3.next = ListNode(4)
l3.next.next = ListNode(2)
