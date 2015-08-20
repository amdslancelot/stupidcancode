def quicksort(a, start):
    print "start=%s" % (start)
    if start == (len(a)-1):
        return

    pivot = len(a)-1
    wall = start
    
    while start != len(a)-2:
        if a[start] < a[len(a)-1]:
            t = a[start]
            a[start] = a[wall]
            a[wall] = t
            wall = wall + 1
        start = start + 1

    if a[len(a)-1] < a[wall]:
        t = a[len(a)-1]
        a[len(a)-1] = a[wall]
        a[wall] = t
        wall = wall + 1

    quicksort(a, wall)

a = [6,5,1,3,8,4,7,9,2]
quicksort(a, 0)
print a
