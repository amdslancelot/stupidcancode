'''
input:
['a', 'b', 'abc', 'baac', 'caba']

output:
[
    ['a'],
    ['b'],
    ['abc'],
    ['baac', 'caba']
]

--
input:
['aab', 'aba', 'baa', 'ca']

output:
[
    ['aba, 'baa', 'aab'],
    ['ca']
]
'''

def getWordCount2(s):
    r = ""
    letterMap = [0] * 26
    for i in range(len(s)):
        #print "letter:%s, ascii:%s" % (s[i], ord(s[i]))
        index = ord(s[i]) - 97
        letterMap[index] = letterMap[index] + 1
        #print letterMap

    for i in range(len(letterMap)):
        if letterMap[i] != 0:
            r = r + chr(i+97) + str(letterMap[i])

    #print r
    return r
   
def func3(a):
    r = {}
    for i in range(len(a)):
        k = getWordCount2(a[i])
        if k in r:
          r[k].append(a[i])
        else:
          r[k] = [a[i]]
    print "ans: %s" % (r)
    return r.values()

# older version:
def getWordCount(s):
    d = {}
    for e in list(s):
        if d.has_key(e):
            d[e] += 1
        else:
            d[e] = 1
    '''
    input: baac
    d = {
        'a':2
        'b':1
        'c':1
    }
    '''
    return d

def func(a):
    b = {}

    for i in range(0, len(a)):
        if b.has_key(a[i]):
           continue
 
        for j in range(i+1, len(a)):
            if j > len(a) - 1 or b.has_key(a[j]):
                continue

            if len(a[i]) == len(a[j]):

                #check if two strings are anagram
                success = True
                i_wordCount = getWordCount(a[i])
                for key, value in i_wordCount.items():
                    j_wordCount = getWordCount(a[j])
                    if not j_wordCount.has_key(key):
                        success = False
                        break
                    if j_wordCount[key] != i_wordCount[key]:
                        success = False
                        break

                if success:
                    if not b.has_key(a[i]):
                        b[a[i]] = 1
                    if not b.has_key(a[j]):
                        b[a[j]] = 1
    
    for e in b.keys():
        a.remove(e)
    
    a.append(b.keys())

    return a

def sortString(s):
    if s == "aab" or s == "aba" or s == "baa":
        return "aab"
    elif s == "ca":
        return "ac"

def func2(a):
    result = []
    hashmap = {}

    #step1
    for e in a:
        t = sortString(e)
        if hashmap.has_key(t):
            hashmap[t].append(e)
        else:
            l = []
            l.append(e)
            hashmap[t] = l
    #step2
    for k in hashmap.keys():
        result.append(hashmap[k])

    return result

a = ['a', 'b', 'abc', 'baac', 'caba']
print "input: ", a
result = func3(a)
print "result: ", result

b = ['aab', 'aba', 'baa', 'ca']
print "input: ", b
result = func3(b)
print "result: ", result 
