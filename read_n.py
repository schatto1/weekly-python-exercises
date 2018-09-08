def read_n(filename, n):
  '''
  Generator function that reads the specified n number of lines at
  a time from a given file
  '''
  f = open(filename)

  while True:
    lines = f.readline()

    if not lines:
      break

    for counter in range(n-1):
      lines += f.readline()

    yield lines

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