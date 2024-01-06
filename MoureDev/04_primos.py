def isCousin(num):
  counter = 0
  for i in range(1, int(num/2)):
    if num % i == 0:
      counter += 1
  return True if counter <= 1 else False

if __name__ == '__main__':
  num = int(input('Number:'))
  print(isCousin(num))