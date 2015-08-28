'''
input: [1,2,3]
output: [[], [1], [1, 2], [1, 2, 3], [1, 3], [2], [2, 3], [3]]
recursively

(hint)
group1: [3]
group2: [[]]
result: [3, []]

group1: [2]
group2: [3, []]
result: [[2,3], [2], [3], []]

group1: [1]
group2: [[2,3], [2], [3], []]
result: [[1,2,3], [1,2], [1,3], [1], [2,3], [2], [3], []]
'''



def superSet(a):
    if len(a) == 0:
        return [[]]
    else:
        t = superSet(a[1:]) #Get all the combinations of sub sets
        new = []
        for e in t:
            new.append(a[:1] + e) #Matching the first element and all elements in sub set together to create new elements
        return new + t #merge 2 sets together

def superSet2(a):
    if len(a) == 0:
        return [[]]
    else:
        t = superSet2(a[:(len(a)-1)])
        new = []
        for e in t:
            new.insert(0, a[(len(a)-1):len(a)] + e)
        return new + t
        
a = [1,2,3]
print sorted(superSet(a))
print superSet(a)
print superSet2(a)

