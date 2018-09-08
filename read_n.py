def read_n(filename):
  '''
  readn_n function.
  '''
  pass

def read_1(filename):
  '''
  Generator function that reads one line from given file
  '''
  f = open(filename)

  while True:
    first_line = f.readline()

    if not first_line:
      break

    yield first_line