'''
"iamhappy" - in
[i, am, happy] - out

[anto] - in
[ant, o] - WRONG out
[an, to] - out

i
ia
iam


boolean dict(String)

1. convert string into an array
2. iterating from the first char in[i]
   if in[i] a word:
        append to result
    else:
        try in[i] + in[i+1]
'''
'''
def a(in, tag):
    if tag == len(in) - 1:
        
'''

def lookUpDict(s):
    print "look up: ", s
    if s == "i":
        return True
    elif s == "am":
        return True
    elif s == "happy":
        return True
    elif s == "an":
        return True
    elif s == "to":
        return True
    else:
        return False

def breakStr(s):
    if s == "":
        return True

    for i in range(1,len(s)+1):
        print i, len(s)
        if lookUpDict(s[:i]) and breakStr(s[i:len(s)+1]):
            return True
    return False

if __name__ == "__main__":
    input = "iamhappy"
    #input = "xxx"
    print breakStr(input)
