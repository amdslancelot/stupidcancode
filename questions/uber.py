'''
"12345678910111213141516..........99100101102....."

def indexOf(num)
return index of num

 3:  2
10:  9
11: 11
12: 13
--
1-10      (n-1-0)*1
11-100   (10-1-0)*1 +   (n-1-9)*2
101-1000 (10-1-0)*1 + (100-1-9)*2 + (n-1-99)*3
'''
def indexOf(num):
    res = 0
    l = len(str(num-1))
    print "l=%s" % (l) 
   
    for i in xrange(1,l+1):
        f = 10**i
        
        t = num
        if num > f:
            t = f

        nines = 0
        for j in xrange(1,i):
            nines += 9*(10**(j-1)) #0=>9=>99=>999...

        add = (t-1-nines)*i
        print "add=(%s-1-%s)*%s=%s" % (t, nines, i, add)

        res += add
        
    return res

r = indexOf(3)
print "3: 2 vs", r
r = indexOf(10)
print "10: 9 vs", r
r = indexOf(11)
print "11: 11 vs", r
r = indexOf(12)
print "12: 13 vs", r
r = indexOf(101)
print "101: 192 vs", r
