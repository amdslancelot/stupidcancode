from math import *

def merge(a):
    print "merge:", a
    l = len(a)
    m = int(round(l / 2))
    b = a[m:]
    a = a[:m]

    print "merge part1:", a
    print "merge part2:", b
    la = len(a)
    lb = len(b)

    ia = 0
    ib = 0
    new = []
    while ia < la and ib < lb:
        if a[ia] > b[ib]:
            new.append(b[ib])
            ib += 1
        else:
            new.append(a[ia])
            ia += 1

    #The rest of items in a
    while ia < la:
        new.append(a[ia])
        ia += 1

    #The rest of items in b
    while ib < lb:
        new.append(b[ib])
        ib += 1

    print "merge ended, return:", new
    return new

def split(a, merging):
    print "split:", a
    l = len(a)
    if l == 2:
        merging = True
    
    if merging:
        return merge(a)
    else:
        m = int(round(l / 2))
        return merge(split(a[:m], merging) + split(a[m:], merging))

a = [6,5,3,1,8,7,2,4]
l = len(a)
print split(a, False)

