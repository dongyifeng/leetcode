# coding=utf-8
print '''
给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

示例 1:

输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
示例 2:

输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
说明:

应当保持奇数节点和偶数节点的相对顺序。
链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。
'''

from LinkedList import *

'''
1. 在奇数位（i 为偶数），将 next （偶数位的结点），加入新的链表，从原链表中删除
2. 将两个链表拼接在一起
'''


def oddEvenList(head):
    if not head or not head.next: return head
    dummy = ListNode(None)
    dummy.next = head
    right = ListNode(None)
    right_node = right
    node = dummy.next
    i = 0
    while node and node.next:
        if i % 2 == 0:
            right_node.next = node.next
            node.next = node.next.next
            right_node = right_node.next
        else:
            node = node.next
        i += 1
    right_node.next = None

    node.next = right.next
    return dummy.next


foreachListNode(oddEvenList(l1))
