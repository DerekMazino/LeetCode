def isAnagram(word1, word2):
  word1 = list(word1)
  word2 = list(word2)
  counter = 0
  for i in word1:
    if i in word2:
      counter += 1
  return True if counter == 4 else False

if __name__ == '__main__':
  word1 = input('Word 1:')
  word2 = input('Word 2:')
  print(isAnagram(word1, word2))