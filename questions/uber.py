'''
"12345678910111213141516..........99100101102....."

def indexOf(num)
return index of num

--
1-10     (n-1)*1
11-100   9+(n-1-9)*2
101-1000 9+(99-9)*2+(n-1-99)*3
'''
def indexOf(num):
    res = 0
    l = len(str(num))
    
    if num<11:
        res += (num-1)%10
    else:
        res += 9

    for i in xrange(1,l):
        if num/(10**i)>0:
            nines = int("9"*(i))
            res += ((num-1)-nines)*(i+1)
        
    return res

print "2 vs", indexOf(3)
print "9 vs", indexOf(10)
print "11 vs", indexOf(11)
print "13 vs", indexOf(12)
print "192 vs", indexOf(101)
