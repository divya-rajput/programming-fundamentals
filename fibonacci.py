# -*- coding: utf-8 -*-
"""
@author Divya Rajput
"""

# For any given value n, find the nth fibonacci value.
# Position: 1 2 3 4 5 6 7 8  9  10 ...
# Value   : 0 1 1 2 3 5 8 13 21 34 ...

# Recursive solution
# TC: O(2^n)
def fibo_recur(n):
    if n<=0:
        return -1
    if n==1 or n==2:
        return n-1
    return fibo_recur(n-2)+ fibo_recur(n-1)

# Iterative solution using array
# TC: O(n), ASC: O(n)
arr=[0,1]
def fibo_arr(n):
    if n<=0:
        return -1
    if n<=len(arr):
        return arr[n-1]
    for _ in range(n-2):
        arr.append(arr[-2]+arr[-1])
    # print(arr)
    return arr[n-1]

# Iterative solution
# TC: O(n), ASC: O(1)
def optimized_fibo(n):
    if n<=0:
        return -1
    if n==1 or n==2:
        return n-1
    # s1=0
    # s2=1
    # s3=-1
    s1, s2, s3 = 0, 1, -1
    for _ in range(n-2):
        s3=s2+s1
        s1=s2
        s2=s3
    return s3

# Test cases
n=10
expected = 34

actual = fibo_recur(n)
assert expected == actual, "Testcase failed: Expected %d, got %d"%(expected, actual)
print("Test Case passed for Recursive Solution")

actual = fibo_arr(n)
assert expected == actual, "Testcase failed: Expected %d, got %d"%(expected, actual)
print("Test Case passed for Iterative Solution with Array")

actual = optimized_fibo(n)
assert expected == actual, "Testcase failed: Expected %d, got %d"%(expected, actual)
print("Test Case passed for Iterative Solution")
