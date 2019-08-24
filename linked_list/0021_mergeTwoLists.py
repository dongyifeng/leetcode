# coding:utf-8



print '''
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''
from LinkedList import *

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


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

# foreachListNode(mergeTwoLists(l1, l2))
foreachListNode(mergeTwoLists(l1, None))
