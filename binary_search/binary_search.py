# coding=utf-8
print '''
给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。


示例 1:

输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
示例 2:

输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
 

提示：

你可以假设 nums 中的所有元素是不重复的。
n 将在 [1, 10000]之间。
nums 的每个元素都将在 [-9999, 9999]之间。
'''

'''
循环
'''


def binary_search(nums, target):
    if not nums or nums[0] > target or nums[-1] < target: return -1
    l = 0
    r = len(nums) - 1
    while l < r:
        mid = (l + r) >> 1
        if nums[mid] == target: return mid
        if nums[mid] > target:
            r = mid - 1
        else:
            l = mid + 1
    return -1


'''
递归
'''


def search2(nums, target, left, right):
    if left > right: return -1
    middle = (left + right) / 2
    if nums[middle] == target: return middle
    if nums[middle] > target:
        return search2(nums, target, left, middle - 1)
    else:
        return search2(nums, target, middle + 1, right)


# n = len([-1, 0, 3, 9, 12])
# print search2([-1, 0, 3, 9, 12], 9, 0, n)

# print search2([-1, 0, 3, 5, 9, 12], -2, 0, len([-1, 0, 3, 5, 9, 12]))


print binary_search([1, 2, 3, 4], 3)

print binary_search([1, 2, 3, 4, 5], 4)

print binary_search([1, 2, 3, 6, 7], 5)
