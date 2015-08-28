'''
Given a string S1 and a string S2, remove all characters in the string S2 which appear in the string S1 and return to the caller.
'''

def func(s1, s2):
    if s1 is None or s2 is None or s1 is "" or s2 is "":
        return s2

    d1 = {}
    for c in list(s1):
        print "c: %s" % (c)
        if not d1.has_key(c):
            d1[str(c)] = 1
        else:
            d1[str(c)] += 1
    
    a2 = list(s2) #convert s2 to an array
    new = ""
    
    #remove all the charecters appeared in s1
    for c in a2:
        if not d1.has_key(c):
            new += c
    
    #result = ""
    #for c in a2:
    #    result.append(c)
        
    return new
    
if __name__ == "__main__":
    #group 1: both of the strings are empty
    #s1 = ""
    #s2 = ""
    
    #group 2: one of the strings is empty
    #s1 = ""
    #s2 = "aabccd"
    
    #group 3: one of the strings is empty
    #s1 = "abc"
    #s2 = ""
    
    #group 4: normal case 1
    #s1 = "abc"
    #s2 = "aabccd"
    
    #group 5: normal case 2
    s1 = "abc"
    s2 = "abcdefg"

    #group 6: two strings are the same
    #s1 = "abc"
    #s2 = "abc"
    
    #group 7: inputs are not strings
    #s1 = 123
    #s2 = 456
    
    print "s1: ", s1
    print "s2: ", s2
    print func(s1, s2)
    
