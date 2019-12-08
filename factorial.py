# -*- coding: utf-8 -*-
"""
@author Divya Rajput

Appendix
range() => range(start_idx, end_idx, steps_to_take)
assert  => assert <condition>, <message_on_assertion_failure> | Raises AssertionError
"""

# For any given number n, find the value of its factorial
# Number: 0 1 2 3 4  5   ...
# Value : 1 1 2 6 24 120 ...

# Recursive solution
# TC: O(2^n)
def fact_recur(n):
    if n<0:
        return 0
    if n==0:
        return 1
    k=1
    for x in range(n):
        k=(x+1)*k
    return k

# Iterative solution using array
# TC: O(n), ASC: O(n)
arr = [1]
def fact_arr(n):
    if n < 0:
        return 0
    # if n == 0:
    #     return 1
    # if len(arr) >= n:
    #     return arr[n]
    for x in range(len(arr)-1, n): # Iterate from len(arr)+1 and keep appending till we reach n-1
        arr.append((x+1)*arr[x])
    return arr[n]
    

# Iterative solution
# TC: O(n), ASC: O(1)
def optimized_fact(n):
    if n < 0:
        return 0
    if n==0:
        return 1
    return n*optimized_fact(n-1)

# Test cases
n=5
expected = 120

actual = fact_recur(n)
assert expected == actual, "Testcase failed: Expected %d, got %d"%(expected, actual)
print("Test Case passed for Recursive Solution")

actual = fact_arr(n)
assert expected == expected, "Testcase failed: Expected %d, got %d"%(expected, actual)
print("Test Case passed for Iterative Solution with Array")

actual = optimized_fact(n)
assert expected == actual, "Testcase failed: Expected %d, got %d"%(expected, actual)
print("Test Case passed for Iterative Solution")
