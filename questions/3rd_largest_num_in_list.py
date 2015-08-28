#List(5,7,8,3,4,2,1,9,12)
#Third largest number in list
#assumption 2: list.length >= 3

'''
To find the largest number : O(n)

(example)
5: (5, 0, 0)
7: (7, 5, 0)
8: (8, 7, 5)
3: (8, 7, 5)

'''

def find3rdLargest(a):
    result = {
        "1" : 0, 
        "2" : 0,
        "3" : 0
    }
    
    for e in a:
        if e > result["1"]: #case: bigger than 1st largest we had
            result["3"] = result["2"]
            result["2"] = result["1"]
            result["1"] = e
        elif e > result["2"]: #case: bigger than the 2nd largest we had
            result["3"] = result["2"]
            result["2"] = e
        elif e > result["3"]: #case: bigger than the 3nd largest we had
            result["3"] = e
        else:
            pass
    
    return result["3"]

a = [5,7,8,3,4,2,1,9,12]
print find3rdLargest(a)
