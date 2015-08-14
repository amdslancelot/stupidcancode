dict = {"mobile","samsung","sam","sung","man","mango","icecream","and","go","i","like","ice","cream","samyang"}
#q = ["ilikesamsung", "iiiiiiii", "ilikelikeimangoiii", "samsungandmango", "samsungandmangok", "ilikesamyangmango"]
q = ["samsungandmangok", "ilikesamyangmango"]

def wordbreak_recursive(s):
  #print "s", s
  if s == "":
    return True

  for i in range(1,len(s)+1):
    #print "s[:%s]=%s" % (i, s[:i])
    if s[:i] in dict and wordbreak_recursive(s[i:len(s)]):
      return True

  #print "False"
  return False

def wordbreak_dp(s):
  map = [False] * (len(s)+1) # +1 becuz we r not using map[0] (to make code more readable)

  for i in range(1, len(s)):
    print "i", i, "s[0:i]", s[0:i]
    if map[i] == False and s[0:i] in dict: # found match!
      map[i] = True
      print "Found match at index=%s, validated string=%s" % (i , s[0:i])

    if map[i] == True:
      print "Look up table and found match at index=%s, validated string=%s" % (i , s[0:i])
      if i == len(s)-1:
        return True #reach end

      for j in range(i+1, len(s)+1):
        print "i", i, "j", j, "s[i:j]", s[i:j]

        if map[j] == False and s[i:j] in dict: # found match!
          map[j] = True
          print "Found match at index=%s, validated string=%s" % (j , s[i:j])

        if map[j] == True and j == len(s): # Reaches the end && Remaining is True
          return True

        #if j == len(s) and map[j]: # Reaches the end
        #  return True

  return False
    

for s in q:
  r1 = wordbreak_recursive(s)
  print "[word break][RC]:", "s:", s, "ans:", r1
  r2 = wordbreak_dp(s)
  print "[word break][DP]:", "s:", s, "ans:", r2
