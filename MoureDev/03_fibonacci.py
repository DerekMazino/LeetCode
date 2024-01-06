if __name__ == '__main__':
  f0 = 0
  f1 = 1
  res = 1
  for i in range(0,50):
    print(res)
    res = f0 + f1
    f0 = f1
    f1 = res


