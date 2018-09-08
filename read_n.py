def read_n(filename):
  '''
  readn_n function.
  '''
  pass

def read_1(filename):
  '''
  Generator function that reads one line at a time from given file
  '''
  f = open(filename)

  while True:
    first_line = f.readline()

    if not first_line:
      break

    yield first_line

def read_2(filename):
  '''
  Generator function that reads two lines at a time from given file
  '''
  f = open(filename)

  while True:
    first_line = f.readline()

    if not first_line:
      break

    second_line = f.readline()

    yield first_line + second_line