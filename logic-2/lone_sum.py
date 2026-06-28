"""
Given 3 int values, a b c, return their sum. 
However, if one of the values is the same as 
another of the values, it does not count towards the sum.
"""
def lone_sum(a,b,c):
    if a != b and b != c and a!= c:
        return a + b + c
    elif a == b and (a == b != c):
        return c
    elif b == c and (b == c != a):
        return a
    elif a == c and (a == c != b):
        return b
    elif (a == b) and (b == c) and (a == c):
        return 0
