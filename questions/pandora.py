'''
a deck
------- 7 feet
------- 7 feet
------- 7 feet
------- 7 feet
------- 7 feet
------- 7 feet
-----   5 feet
-----   5 feet
-----   5 feet
------  6 feet
------  6 feet
------  6 feet

 8 feet = $13
12 feet = $15
16 feet = $17

find a solution has lowest cost
'''
def checkFinished(bp):
    for key, value in bp.items():
        print "checking...%s : %s\n" % (key, value)
        if value != 0:
            return False
    return True


def getLowestCost(blueprint, result):
    if checkFinished(blueprint):
        return result

    

    
    

if __name__ == "__main__":
    blueprint = {
        "7" : 6,
        "5" : 3,
        "6" : 3,
    }
    
    result = {
        "8" : [ 13, 0 ],
        "12" : [ 15, 0 ],
        "16" : [ 17, 0 ],
    }
    getLowestCost(blueprint, result)
