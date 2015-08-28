'''
Recursively reverse an array
'''

def reverse(a, first, last):
    print "a:%s, first:%s, last:%s" % (a, first, last)
    if first == last or first-1 == last:
        return a
    else:
        tmp = a[first]
        a[first] = a[last]
        a[last] = tmp
        return reverse(a, first+1, last-1)

def reverse2(a, i):
    if i>(int(len(a)/2)-1): #return ending case
        return a
    else: #return all other cases
        t = a[i]
        a[i] = a[len(a)-i-1]
        a[len(a)-i-1] = t
        return reverse2(a,i+1)
    
a = [3,5,7,9,11,13]
l = len(a)
print reverse(a, 0, l-1)

print reverse2(a,0)
