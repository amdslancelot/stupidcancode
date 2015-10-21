# Write a function that returns the seconds largest element in the array.
# For example, given the array [2, 5, 1, 10, 7, 9], the function should return 9.


# [2, 5, 1, 9, 9, 7]
#           ^
# res = [9,5]
# [3,3,3]

import sys
def func(nums):
    if len(nums) < 2:
        exit(1)
    
    res = [-sys.maxint, -sys.maxint]
    for x in nums:
        if x > res[0]:
            t = res[0]
            res[0] = x
            res[1] = t
            continue
        if res[0] > x > res[1]:
            res[1] = x
    if res[1] != -sys.maxint:
        return res[1]
    else:
        exit(1)
    
