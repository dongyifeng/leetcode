# coding:utf-8

from LinkedList import *

'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。
'''


# 链表快慢指针:O(n)
# 技巧一：快慢指针
# 技巧二：哑变量：省去了删除节点是头结点的判断
def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    fast = slow = dummy
    # fast 指针先走 n + 1 步
    for i in range(n + 1):
        fast = fast.next

    # fast 与 slow 间隔 n 个元素，fast 和 slow 同时走到终点。
    while fast:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return dummy.next


print "---"
foreachListNode(removeNthFromEnd(l1, 2))

print "---"
h1 = ListNode(1)
foreachListNode(removeNthFromEnd(l1, 1))
