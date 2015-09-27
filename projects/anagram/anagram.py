import re, argparse

class FindAnagram:
  def __init__(self):
    self.most_num_of_words = []
    self.just_two_words = []
    self.just_two_words_final = False
    self.arr = self.get_word_list()

  def word_to_letter_map(self, word):
    word = re.sub('[^A-Za-z0-9]+', '', word.lower())
    print "word:", word

    alphabets_i = [0]*26
    for w in word:
      t = ord(w)-97
      alphabets_i[t] += 1
    print word, alphabets_i

    return alphabets_i

  def get_word_list(self):
    with open("words.txt") as fh:
      print fh.read().count("\n")
      fh.seek(0,0)

      arr = fh.read().split("\n")
      for i in xrange(len(arr)):
        arr[i] = re.sub('[^A-Za-z0-9]+', '', arr[i].lower())

      return arr
    return None

  def func(self, word):
    alphabets_i = self.word_to_letter_map(word)
    dp = {}
    collect = []
    l = len(self.arr)
    for j in xrange(l):
      if len(self.arr[j]) <= 1:
        continue
      if word == self.arr[j]:
        continue
      if len(word) < len(self.arr[j]):
        continue
      if word == self.arr[j]:
        continue
      if self.arr[j] in dp:
        continue
      dp[self.arr[j]] = 1
      print "%s vs arr[%s]=%s, letters=%s" % (word, j, self.arr[j], alphabets_i)

      alphabets_i_clone = self.clone(alphabets_i)

      #check if any letters not in alphabets chart
      isAllLettersValid = True
      for w in self.arr[j].lower():
        t = ord(w)-97
        if alphabets_i_clone[t] == 0:
          isAllLettersValid = False
          break
        alphabets_i_clone[ord(w)-97] -= 1
        #word = word.replace(w, "")

      print "isAllLettersValid:", isAllLettersValid

      if isAllLettersValid: #no non-existed letters
        alphabets_i = alphabets_i_clone
        collect.append(self.arr[j]) #add
      else: #there is non-existed letters
        continue
  
      print "collect:", collect
      if self.isFinished(alphabets_i): #no letters left
        if len(collect) == 2 and not self.just_two_words_final:
          self.just_two_words = collect
          self.just_two_words_final = True
        if len(collect) > len(self.most_num_of_words):
          self.most_num_of_words = collect
        return
      else: #still has letters left
        #self.func(word)
        continue #Keep searching

  def isFinished(self, chart):
    for k in xrange(26): #check if has unfinished letters
      if chart[k] > 0:
        return False
    return True

  def clone(self, arr):
    arr_new = [0]*len(arr)
    for k in xrange(len(arr)):
      arr_new[k] = arr[k]
    return arr_new

  def result(self):
    '''
    if len(self.just_two_words) == 0:
      print "most_num_of_words:"
      print "just_two_words:"
      return
    '''
    print "most_num_of_words:", " ".join(self.most_num_of_words)
    print "just_two_words:", " ".join(self.just_two_words)
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="Find Most Number Anagram and Just Two Words Anagram", description="given a word from a wordlist, find one anagram with the most number of words (from the given wordlist) and one anagram with just  two words in them (if one exists). If no anagrams exist with two or more words, the program should print an empty string for both cases.")

  parser.add_argument("word", help="The given word in the word list")
  args = parser.parse_args()
  
  s = FindAnagram()
  s.func(args.word)
  #s.func("abactinally")
  s.result()
