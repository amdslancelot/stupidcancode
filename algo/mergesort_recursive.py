'''
Due to the Merge Sort implementations I found on the internet are all non-recursive versions,
so I decided to write one by my own, without refercing anyone's code, starting from scratch.
'''

from math import *

def merge(a):
    if len(a) < 2:
        return a

    print "merge:", a
    m = int(len(a) / 2)
    b = a[m:]
    a = a[:m]

    print "merge part1:", a
    print "merge part2:", b
    ia = 0
    ib = 0
    new = []
    while ia < len(a) and ib < len(b):
        if a[ia] > b[ib]:
            new.append(b[ib])
            ib += 1
        else:
            new.append(a[ia])
            ia += 1

    new += a[ia:] #The rest of items in a
    new += b[ib:] #The rest of items in b

    print "merge ended, return:", new
    return new

def mergeSort1(a, merging):
    print "mergeSort1:", a
    if len(a) == 2:
        merging = True
    
    if merging:
        print "merging!"
        return merge(a)
    else:
        m = int(len(a) / 2)
        return merge( mergeSort1(a[:m], merging) + mergeSort1(a[m:], merging) ) # recursive + helper function

def mergeSort2(a):
    if len(a) < 2:
        return a
    else:
        m = int(len(a)/2)
        return merge( mergeSort2(a[:m]) + mergeSort2(a[m:]) ) # recursive + helper function

a = [6,5,3,1,8,7,2,4]
l = len(a)
print "1:"
print mergeSort1(a, False)
print
print "2:"
print mergeSort2(a)
