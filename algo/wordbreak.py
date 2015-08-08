dict = {"mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream"}
q = ["ilikesamsung", "iiiiiiii", "ilikelikeimangoiii", "samsungandmango", "samsungandmangok"]

def contains(s, start, end):
  #print len(s), "start", start, "end", end, s[start:end]
  if s[start:end] in dict:
    if end == len(s):
      return True
    else:
      return contains(s, end, end+1)
  else:
    if end == len(s):
      return False
    else:
      return contains(s, start, end+1)

def wordbreak_recursive(s):
  start = 0
  end = start+1

  return contains(s, start, end)

def wordbreak_dp(s):
  map = [False] * (len(s)+1) # +1 becuz we r not using map[0] (to make code more readable)

  for i in range(1, len(s)):
    #print "i", i, "s[0:i]", s[0:i]
    if map[i] == False and s[0:i] in dict: # found match!
      map[i] = True
      #print "map[%s]=%s" % (i , map[i])

    if map[i] == True:
      #print "map[%s]=%s i again" % (i , map[i])
      if i == len(s)-1:
        return True #reach end

      for j in range(i+1, len(s)+1):
        #print "j", j, "s[i:j]", s[i:j]

        if map[j] == False and s[i:j] in dict: # found match!
          map[j] = True
          #print "map[%s]=%s" % (j, map[j])
          i = j

        if map[j] == False and j == len(s): # Reaches the end && Remaining is False 
          return False
        
        if map[j] == True:
          #print "map[%s]=%s j again" % (j, map[j])
          i = j # Make the loop starts from where we found match
          if j == len(s): # Reaches the end && Remaining is True
            return True

  return False
    

for s in q:
  r1 = wordbreak_recursive(s)
  print "word break rc:", "s:", s, "ans:", r1
  r2 = wordbreak_dp(s)
  print "word break dp:", "s:", s, "ans:", r2
