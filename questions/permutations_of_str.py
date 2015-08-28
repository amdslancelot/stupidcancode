'''
Write a program to generate permutations of a string.
'''

def permutations(prefix, s):
    if s == "":
        print prefix
        return
    
    for i in range(len(s)):
        #print "prefix=%s, word=%s" % (s[i], prefix+s[i]+s[:i]+s[i+1:])
        permutations(prefix+s[i], s[:i]+s[i+1:])
        

def gen(s):
    if len(s) == 0:
        return []
    else:
        new = []
        t = s[1:] #rest
        rest = gen(t) #recursive
        print "prefix: %s, rest: %s" % (s[:1], rest)
        if len(rest) == 0:
            new.append(s[:1])
        else:
            for e in rest:
                l = len(e)
                print "e=%s" % (e)
                for i in range(0, l+1):
                    print "i=%s" % (i)
                    new.append(e[0:i] + s[:1] + e[i:l])

        return new

s = "abc"
#print gen(s)
print permutations("", s)
