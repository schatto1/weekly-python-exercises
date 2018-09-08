def read_one(filename):
  '''
  This function opens the specified file in parameter filename,
  and reads each line within the file one by one and prints to
  the console.
  '''
  for one_line in open(filename):
    print(one_line.rstrip())