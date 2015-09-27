import re, argparse

class FindAnagram:
  def __init__(self, fname):
    self.most_num_of_words = []
    self.just_two_words = []
    self.just_two_words_final = False
    self.arr = self.get_word_list(fname)
    self.dp = {}

  def word_to_letter_map(self, word):
    word = re.sub('[^A-Za-z0-9]+', '', word.lower())

    alphabets = [0]*26
    for w in word:
      t = ord(w)-97
      alphabets[t] += 1

    return alphabets

  def get_word_list(self, fname="words.txt"):
    with open(fname) as fh:
      fh.seek(0,0)

      arr = fh.read().split("\n")
      for i in xrange(len(arr)):
        arr[i] = re.sub('[^A-Za-z0-9]+', '', arr[i].lower())

      return arr
    return None

  def validate(self, word, j):
    if len(self.arr[j]) <= 1:
      return False
    if len(word) < len(self.arr[j]):
      return False
    return True

  def find(self, word, collect):
    if len(word) == 1:
      return

    if word == "":
      if len(collect) == 2 and not self.just_two_words_final:
        self.just_two_words = collect
        self.just_two_words_final = True
      if len(collect) > len(self.most_num_of_words):
        self.most_num_of_words = collect
      return

    alphabets = self.word_to_letter_map(word)
    l = len(self.arr)
    for j in xrange(l):
      if not self.validate(word, j):
        continue

      alphabets_clone = self.clone(alphabets)
      new_word = word

      #check if any letters not in alphabets chart
      isAllLettersValid = True
      for w in self.arr[j]:
        t = ord(w)-97
        if alphabets_clone[t] == 0:
          isAllLettersValid = False
          break
        alphabets_clone[t] -= 1
        new_word = new_word.replace(w, "")

      if isAllLettersValid: #no non-existed letters
        self.find(new_word, collect + [self.arr[j]])
  
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
    if len(self.just_two_words) == 0:
      print "Most Number of Words:"
      print "Just Two Words:"
      return
    print "Most Number of Words:", " ".join(self.most_num_of_words)
    print "Just Two Words:", " ".join(self.just_two_words)
    
if __name__ == "__main__":
  parser = argparse.ArgumentParser(prog="Find Most Number Anagram and Just Two Words Anagram", description="given a word from a wordlist, find one anagram with the most number of words (from the given wordlist) and one anagram with just  two words in them (if one exists). If no anagrams exist with two or more words, the program should print an empty string for both cases.")

  parser.add_argument("word", help="The given word in the word list")
  parser.add_argument("-f", type=str, 
                      help="source file name")
  args = parser.parse_args()

  s = None
  if args.f:
    s = FindAnagram(args.f)
  else:
    s = FindAnagram("words.txt")
  s.find(args.word, [])
  s.result()
