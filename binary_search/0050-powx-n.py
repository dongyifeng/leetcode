# coding=utf-8
print '''
实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:

输入: 2.00000, 10
输出: 1024.00000
示例 2:

输入: 2.10000, 3
输出: 9.26100
示例 3:

输入: 2.00000, -2
输出: 0.25000
解释: 2-2 = 1/22 = 1/4 = 0.25
说明:

-100.0 < x < 100.0
n 是 32 位有符号整数，其数值范围是 [−231, 231 − 1] 。
'''


def myPow(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    return x ** n


'''
暴力
'''


def myPow2(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    x = x if n > 0 else 1.0 / x
    s = x
    for i in range(abs(n) - 1):
        s *= x
    return s


'''
折半

原理：x ^(n+m) = x^n * x^m
将指乘积转化为加法

'''


def myPow3(x, n):
    """
    :type x: float
    :type n: int
    :rtype: float
    """
    res = x
    i = n
    while i >0:
        if i % 2 != 0:
            i -= 1
            res *= x
        else:
            i >>= 1
            res = res * res
        # print i

    return res if n > 0 else 1.0 / res


# print myPow2(2, 10)
#
# print myPow2(2.1, 3)
#
# print myPow2(2, -2)

# print myPow2(0.0001, 2147483647)

# print 0.0001 ** 2147483647

print myPow3(2, 10)

print myPow3(2.1, 3)

print myPow3(2, -2)

# print myPow2(0.0001, 2147483647)
