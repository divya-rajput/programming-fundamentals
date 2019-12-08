# -*- coding: utf-8 -*-
"""
@author Divya Rajput
"""

# For any given natural number n, print the pattern:
# For n = 3
# ***
# **
# *
def Patterns(n):
    for i in range(n):
        for _ in range(n-i):
            print("*",end='')
        print()

# For any given natural number n, print the pattern:
# For n = 3
# *
# **
# ***
def inv_Pattern(n):
    for i in range(n):
        for _ in range(i+1):
            print("*",end='')
        print()

# For any given natural number n, print the pattern:
# For n = 3
# *****
#  ***
#   *
def cone_pattern(n):
    for i in range(n):
        for _ in range(i):
            print(" ",end="")
        for _ in range(2*(n-i)-1):
            print("*",end="")
        print()
    
# Taking inputs from stdin        
n = int(input())

print()
Patterns(n)
print()
inv_Pattern(n)
print()
cone_pattern(n)