'''
Pseudocode for ISBN Checker
1. Obtain user input
2. Remove non-int characters from input string
3. Make sure user input contains 13 digits
4. Go through first 12 digits and multiply each second digit by 3
5. Sum the first 12 digits
6. Divide by 10, keep remainder
7. Subtract remainder from 10
8. Check result with checksum (13th digit)
9. Return corresponding result
'''

# Import all necessary packages
import re

def validate_isbn(isbn_string):
    # Import necessary regex package
    import re

    # Strip string of all non-numeric chars
    isbn_string = re.sub(r"\D", "", isbn_string)

    # Throw exception if not 13 digits
    if len(isbn_string) != 13:
        raise TypeError(f"Your input should contain a 13 digits, not {len(isbn_string)}")

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


# put the below code in solution.py
# put your solution (the function validate_isbn) above it
# run it from the command line with "pytest solution.py'

import pytest

@pytest.mark.parametrize('isbn', [
    '',
    '12345',
    '123456789012345',
    ])
def test_bad_isbn_length(isbn):
    with pytest.raises(TypeError) as e:
        validate_isbn(isbn)
    assert e.value.args[0].endswith(f', not {len(isbn)}')

@pytest.mark.parametrize('isbn', [
    '9780143127796',
    '9780415700108',
    '9780525533184',
    ])
def test_good_isbn(isbn):
    assert validate_isbn(isbn)

@pytest.mark.parametrize('isbn', [
    '9780143127793',
    '9780415700103',
    '9780525533183',
    ])
def test_bad_isbn(isbn):
    assert validate_isbn(isbn) == False
