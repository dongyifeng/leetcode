# coding=utf-8
print '''
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

你的算法时间复杂度必须是 O(log n) 级别。

如果数组中不存在目标值，返回 [-1, -1]。

示例 1:

输入: nums = [5,7,7,8,8,10], target = 8
输出: [3,4]
示例 2:

输入: nums = [5,7,7,8,8,10], target = 6
输出: [-1,-1]
'''


def searchRange(nums, target):
    if not nums or nums[0] > target or nums[-1] < target: return [-1, -1]
    start = 0
    end = len(nums)
    mid = end >> 1
    f = False
    while start <= mid <= end:
        if nums[mid] == target:
            f = True
            break
        if nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        mid = (start + end) >> 1
    if not f: return [-1, -1]

    i = j = mid

    while i >= 0:
        if nums[i] == target:
            i -= 1
        else:
            break
    while j < len(nums):
        if nums[j] == target:
            j += 1
        else:
            break
    return [i + 1, j - 1]


print searchRange([1, 4], 4)

# print searchRange([8], 8)
#
# print searchRange([2, 2], 2)
#
# print searchRange([2, 2], 9)
#
# print searchRange([5, 7, 7, 8, 8, 10], 8)
# #
# print searchRange([5, 7, 7, 8, 8, 10], 6)
