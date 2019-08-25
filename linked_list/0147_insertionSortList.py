# coding=utf-8
print '''
对链表进行插入排序

插入排序算法：

1. 插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
2. 每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
3. 重复直到所有输入数据插入完为止。
'''

from LinkedList import *


def insert(head, lastNode):
    node = head
    while node and node.next:
        if node.next.val >= lastNode.val:
            lastNode.next = node.next
            node.next = lastNode
            return
        node = node.next
    return


def insertionSortList(head):
    if not head or not head.next: return head

    dump = ListNode(None)
    dump.next = head

    node = head
    while node and node.next:
        if node.next.val <= node.val:
            # 删除结点
            insert_node = node.next
            node.next = node.next.next
            # 插入节点
            insert(dump, insert_node)
        else:
            node = node.next
    return dump.next



l1 = ListNode(4)
l1.next = ListNode(2)
l1.next.next = ListNode(1)
l1.next.next.next = ListNode(3)

foreachListNode(insertionSortList(l1))

l2 = ListNode(-1)
l2.next = ListNode(5)
l2.next.next = ListNode(3)
l2.next.next.next = ListNode(4)
l2.next.next.next.next = ListNode(0)

foreachListNode(insertionSortList(l2))