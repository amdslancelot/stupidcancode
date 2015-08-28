'''
Given a list of several letters.
Write a function getTile() to randomly pick one letter from the list everytime calling it.

Time complexity for:
1. access the picked element
2. maintaining the list 

both have to be O(1)
'''

from random import uniform
def getTile(a):
    '''
    m = {}
    for e in a:
        if m.has_key(e):
            m[e] += 1
        else:
            m[e] = 1
    print m
    '''

    i = int(uniform(0, len(a)-1))
    print i

    #swap
    al = len(a)
    t = a[al-1]
    a[al-1] = a[i]
    a[i] = t

    return a.pop()

def getTile2(a):
    #build a map
    m = {}
    for e in a:
        if m.has_key(e):
            m[e] += 1
        else:
            m[e] = 1
    print m

    l = 0
    for k,i in m.items():
        l += len(i)
    print l

    


a = ["A", "A", "A", "A", "A", "B", "B", "Z"]
print a
poped = getTile(a)
print "poped: ", poped
print a


