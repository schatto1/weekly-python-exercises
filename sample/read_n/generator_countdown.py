def countdown(num):
  print('Starting')
  while num > 0:
    yield num
    num -= 1