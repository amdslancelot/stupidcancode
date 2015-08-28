'''
given: maximum bandwidth, list of reservations -- can these reservations be satisfied together?

example:
max_bw = 40
reservations:
start end amount
5 9 10
6 12 20
3 15 20 

(from time 6 to 9 in this example, we have 50 units requested but only 40 available)

return False
'''
#example usage:
# isSatisfiable(max_bw=40, reservations=[(1,5,10),(2,5,20)...])

def isSatisfied(max_bw, reservations):
    schedule = {}
    
    for r in reservations:
        start = r[0]
        end = r[1]
        amount = r[2]
        
        # putting all the traffic into timestamps
        for t in range(start, end):
            if !schedule.has_key(str(start)):
                schedule[str(t)] = amount
            else:
                schedule[str(t)] += amount
                if schedule[str(t)] > max_bw:
                    return False

    '''
    # check if any timestamp exceed the bandwidth            
    for i, v in schedule.iteritems():
        if v > max_bw:
            return False
    '''
    return True
    

