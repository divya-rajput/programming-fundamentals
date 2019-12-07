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
# arr=[1,2,3,4,5]
# def fact_arr(n):
#     if n<0:
#         return 0
#     if n==0:
#         return arr[0]
#     for x in range(n):
#         arr.append(n*arr[x])
#     return arr[-1]
    

# Iterative solution
# TC: O(n), ASC: O(1)
def optimized_fact(n):
    if n<0:
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

# actual = fact_arr(n)
# assert expected == actual, "Testcase failed: Expected %d, got %d"%(expected, actual)
# print("Test Case passed for Iterative Solution with Array")

actual = optimized_fact(n)
assert expected == actual, "Testcase failed: Expected %d, got %d"%(expected, actual)
print("Test Case passed for Iterative Solution")
