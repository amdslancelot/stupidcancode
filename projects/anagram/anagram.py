import re

most_num_of_words = ""
most_num_of_words_count = 0
just_two_words_final = []

def func():
  with open("words.txt") as fh:
    print fh.read().count("\n")
    fh.seek(0,0)

    arr = fh.read().split("\n")
    for i in xrange(len(arr)):
      arr[i] = re.sub('[^A-Za-z0-9]+', '', arr[i].lower())

    l = len(arr)
    #print arr
    for i in xrange(l):
      if len(arr[i]) <= 1:
        continue
      alphabets_i = [0]*26
      for w in arr[i]:
        if w == '':
          continue
        t = ord(w)-97
        if t not in xrange(len(alphabets_i)):
          print "error:", arr[i]
          exit(1)
        alphabets_i[t] += 1
      print arr[i], alphabets_i
    
      dp = {}
      just_two_words = []
    
      for j in xrange(l):
        if len(arr[j]) <= 1:
          continue
        if i == j:
          continue
        if arr[i] == arr[j]:
          continue
        #print "test: arr[%s]=%s vs arr[%s]=%s" % (i, arr[i], j, arr[j])
        if len(arr[i]) < len(arr[j]):
          continue
        if arr[i].lower() == arr[j].lower():
          continue
        if arr[j] in dp:
          continue
        dp[arr[j]] = 1
        #print "arr[%s]=%s vs arr[%s]=%s, letters=%s" % (i, arr[i], j, arr[j], alphabets_i)

     
        #clone alphabets_i
        alphabets_i_clone = clone(alphabets_i)

        #check if any letters not in alphabets_i
        go = True
        for w in arr[j].lower():
          t = ord(w)-97
          if alphabets_i_clone[t] == 0:
            go = False
            break
          alphabets_i_clone[ord(w)-97] -= 1

        #print "2", go

        if go: #no non-existed letters
          go = False

          alphabets_i = alphabets_i_clone
          just_two_words.append(arr[j])

          for k in xrange(26): #check if has unfinished letters
            if alphabets_i[k] > 0:
              go = True
              break
        else:
          continue
    
        print "just_two_words:", just_two_words
        print "3", go
        if go: #still has letters left
          if len(just_two_words) == 2:
            break
          continue
        else: #no letters left
          if len(just_two_words) == 2:
            return just_two_words
          return []

    return just_two_words
            
    
def clone(arr):
  arr_new = [0]*len(arr)
  for k in xrange(len(arr)):
    arr_new[k] = arr[k]
  return arr_new
      
      
r = func()
print "ans:", r
        
    

  #for line in fh:
  #  if line_count != target_count:
      
    
