# Import all necessary packages
import re

def check_isbn(isbn_string):
    # Strip string of all non-numeric chars
    isbn_string = re.sub(r"\D", "", isbn_string)

    # Throw exception if not 13 digits
    if len(isbn_string) != 13:
        return f"bad length of {len(isbn_string)}"

    # got 13 digits, keep going with program
    isbn_digits = []
    checksum = 0
    for counter, digit in enumerate(isbn_string, 1):
        if counter % 2 == 0:
            isbn_digits.append(int(digit) * 3)
        elif counter == len(isbn_string):
            checksum = int(digit)
        else:
            isbn_digits.append(int(digit))

    calculation = 10 - (sum(isbn_digits) % 10)

    if calculation == checksum:
        return True
    else:
        return False

def validate_isbns(*args):
    # open file to append to using first argument
    argsiter = iter(args)
    outfile = next(argsiter)

    with open(outfile, "a") as output:
        for isbn in argsiter:
            output.write(isbn + "\t" + str(check_isbn(isbn)) + "\n")

    print("Report has been created.")
    return

# put the below code in solution.py
# put your solution (the function validate_isbn) above it
# run it from the command line with "pytest solution.py'

import pytest

def test_isbn_checker(tmp_path):
    test_directory = tmp_path / 'testfiles'
    test_directory.mkdir()
    filename = test_directory / 'outfile.txt'

    test_isbns = {'': 'bad length of 0',          # empty; invalid
                  '12345': 'bad length of 5',
                  '123456789012345' : 'bad length of 15',
                  '9780143127796': 'True',
                  '9780415700108': 'True',
                  '9780525533184': 'True',
                  '9780143127793': 'False',
                  '9780415700103': 'False',
                  '9780525533183': 'False' }

    validate_isbns(filename, *test_isbns)

    for one_line in open(filename):
        print(one_line)
        isbn, assessment = one_line.rstrip().split('\t')

        assert assessment == test_isbns[isbn]
