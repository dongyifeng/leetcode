# coding=utf-8
print '''
请判断一个链表是否为回文链表。

示例 1:

输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

from LinkedList import *


# 从链表中间断开。成两个链表
# 翻转其中一个链表。
# 逐个比较两个链表是否相等
def isPalindrome(head):
    if not head: return True
    dump = ListNode(None)
    dump.next = head
    slow = fast = dump
    pre = None
    while fast and fast.next:
        fast = fast.next.next
        pre = slow
        slow = slow.next

    if fast:
        right_sub = slow.next
        slow.next = None
    else:
        pre.next = None
        right_sub = slow.next

    right_sub, right_node_end = reverseList(right_sub)

    left_node = dump.next
    right_node = right_sub
    while left_node and right_node:
        if left_node.val != right_node.val:
            return False
        left_node = left_node.next
        right_node = right_node.next
    return True


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(2)
l1.next.next.next.next = ListNode(1)

print isPalindrome(l1)

l2 = ListNode(1)
l2.next = ListNode(2)
l2.next.next = ListNode(2)
l2.next.next.next = ListNode(1)

print isPalindrome(l2)
