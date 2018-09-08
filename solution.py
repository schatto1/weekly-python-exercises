def read_n(filename, n):
  '''
  Solution by Mr. Lerner to the generator function exercise.
  Generator function that opens a file and reads the specified number
  of lines at each time
  '''

  f = open(filename)

  while True:
    output = ''.join(f.readline()
                     for i in range(n))
    if output:
      yield output
    else:
      break