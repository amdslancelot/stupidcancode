'''
Find the smallest positive missing number

Time Complexity: O(n)
'''

def seperate(a):
  t = 0
  j = 0
  for i in range(0,len(a)):
    if a[i] > 0:
      if i != j:
        t = a[i]
        a[i] = a[j]
        a[j] = t
      j = j+1
  return j

def smallestPositiveMissingNumber(a, end):
  for i in range(0, end):
    if abs(a[i]) < end:
      a[abs(a[i])-1] = a[abs(a[i])-1] * -1

  for i in range(0, end):
    if a[i] > 0:
      return i+1

  return -1

a = [2, 3, -7, 6, 8, 1, -10, 15]
end = seperate(a)
print a
print "seperated", end
print "smallestPositiveMissingNumber", smallestPositiveMissingNumber(a, end)
