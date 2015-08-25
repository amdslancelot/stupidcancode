def quicksort(a, start, end):
    print
    print "start=%s, end=%s" % (start, end)
    if start == end or start > end:
        return

    wall = start
    index = start
    
    while index != end:
        print "index", index, "wall", wall
        if a[index] < a[end]:
            t = a[index]
            a[index] = a[wall]
            a[wall] = t
            wall = wall + 1
        index = index + 1

    print "end", end, "wall", wall
    if a[end] < a[wall]:
        t = a[end]
        a[end] = a[wall]
        a[wall] = t

    print "wall=%s, a: %s" % (wall, a)

    quicksort(a, start, wall-1)
    quicksort(a, wall+1, end)


#a = [6,5,1,3,8,4,7,9,2]
#a = [6,5,1,3,2,4,7,9,8]
a = [12,47,85,23,67,43,45,77]
print "origin: %s" % (a)
quicksort(a, 0, len(a)-1)
print a
