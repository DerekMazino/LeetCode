if __name__ == '__main__':
  word = input('Ingresa una palabra: \n')
  inverted_word = ''
  for i in range(len(word)-1,-1,-1):
    inverted_word += word[i]
  print(inverted_word)