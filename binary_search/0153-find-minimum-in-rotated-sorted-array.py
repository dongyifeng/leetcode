# coding=utf-8
print '''
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

请找出其中最小的元素。

你可以假设数组中不存在重复元素。

示例 1:

输入: [3,4,5,1,2]
输出: 1
示例 2:

输入: [4,5,6,7,0,1,2]
输出: 0
'''

import sys


def findMin(nums):
    rotation_index = 0
    last = nums[0]
    # 判断是否旋转
    for i in range(1, len(nums)):
        if last > nums[i]:
            rotation_index = i
            break
        last = nums[i]
    return min(nums[0], nums[rotation_index])


print findMin([3, 4, 5, 1, 2])
