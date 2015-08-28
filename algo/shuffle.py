'''
Given a list, shuffle that

0, 1, ...  999999

count = 999999
'''


import random
def shuffle(list):
  print(list)
  l = len(list)
  temp = 0
  
  for i in range(l-1, 1, -1):
  #for i in range(0, l): # Not good
    n = int(random.uniform(0, i))
    print "list[%s]=%s and list[%s]=%s switch content." % (n, list[n], i, list[i])
    
    temp = list[i]
    list[i] = list[n]
    list[n] = temp
    print "after switch: ", list
  
  return list

print shuffle(range(10))
