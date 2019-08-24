# coding:utf-8

print '''
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
'''

from LinkedList import *

import heapq
import sys


# 采用冒泡选取最小队列
def mergeKLists1(lists):
    if not lists: return
    node = head = ListNode(0)
    while True:
        min_li = ListNode(sys.maxint)
        k = 0
        for i in range(len(lists)):
            li = lists[i]
            if not li: continue
            if li.val < min_li.val:
                min_li = li
                k = i
        if min_li.val != sys.maxint:
            node.next = min_li
            node = node.next
            min_li = min_li.next
            lists[k] = min_li
        lists = [li for li in lists if li]
        if len(lists) <= 1: break

    if lists:
        node.next = lists[0]
    return head.next


# 采用最小堆选取最小队列
def mergeKLists2(lists):
    if not lists: return
    node = head = ListNode(0)
    heap = [(li.val, li) for li in lists if li]
    heapq.heapify(heap)
    while heap:
        val, li = heapq.heappop(heap)
        node.next = li
        node = node.next
        li = li.next
        if li:
            heapq.heappush(heap, (li.val, li))

    return head.next


l1 = ListNode(1)
l1.next = ListNode(4)
l1.next.next = ListNode(5)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)

l3 = ListNode(2)
l3.next = ListNode(6)

lists = [l1, l2, l3]

# foreachListNode(mergeKLists1(lists))

foreachListNode(mergeKLists2(lists))


def HeapSort(list):
    # 将 list 构建成堆
    heapq.heapify(list)
    heap = []
    while list:
        heap.append(heapq.heappop(lists))
    list[:] = heap
    return list

from Queue import PriorityQueue

q = PriorityQueue()
q.put(1)
q.put(5)
q.put(4)
q.put(3)

print q.task_done()




