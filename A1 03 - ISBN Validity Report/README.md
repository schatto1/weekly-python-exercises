# ISBN Validity Report
This is my solution to Reuven Lerner's Weekly Python Exercise A1 Week 3 Exercise, `ISBN Validity Report`.

The prompt was to create a script containing a function `validate_isbns` that creates and writes a file containing the validity of a list of 13-digit ISBNs provided by user input.

The last digit of a 13-digit ISBN is a "checksum", where the digit depends on the first 12 digits of the ISBN. Every other digit of the ISBN is multiplied by 3, with the first 12 digits summed together. This total is then divided by 10, and the remainder kept. This remainder is then subtracted from 10. If the resulting integer is identical to the checksum (the 13th digit), then the provided number is a valid ISBN.

The `validate_isbns` function performs the above operations on the user-provided numbers to see if each input is a valid ISBN, and creates a report that contains the results.

## Getting Started

These instructions will get you a copy of the code on your local machine for further modification, development, and testing.

### Prerequisites

1. Python 3.
2. Installed "pytest" module in system.

### Installing

Download the file `check_isbns.py` to a desired project location.

### Usage

1. Proceed to the desired project location in your terminal.
2. Test the function by entering "python3 pytest -vv check_isbns.py".

## Original Prompt

Below, to quote Mr. Lerner:

>Last week, we turned our ISBN checker into a function, such that we could call it and have it tell us whether an ISBN was accurate or not.
>
>This week, I want you to write a new, related function called `check_isbns`.  Notice that the function name implies that we're going to accept a number of ISBNs passed to us. But this function will actually take two arguments:
> - the first argument is a string, naming the file into which the function should print its report
> - all further arguments are ISBNs that should be checked
>
>In other words, we can call this function with a number of arguments, each of which will be checked to see if it's a valid ISBN.  The function will put its assessment of each ISBN in a file.  Each line in the file will contain two values, the ISBN being checked and one of three values:
> - True (indicating it's valid)
> - False (indicating it's not valid)
> - bad length of x (where "x" is the length, and it's not 13)
>
>In other words, I can say:
```shell
check_isbns('mybooks.txt', '12345', '9780525533184', '9780143127793')
```
>
>and if I do so, then the file will contain three lines:
```shell
    12345    bad length of 5
    9780525533184    True
    9780143127799    False
```
>
>This week's exercise introduces two different major ideas:
> - writing a function that takes a variable number of arguments using \*args
> - writing to a file, ideally using the "with" construct
>
>The function will remain largely the same from last week, but will clearly need to be modified to handle the different number of arguments, as well as the new functionality.
>
>If you're new to some of these ideas, here are some good sources:
>
> - Working with files: https://stackabuse.com/writing-files-using-python/
> - Accepting \*args: https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3
>
>Note that we won't be using \*\*kwargs in this course.  (That'll be in course A2.)  So in the second tutorial, you can ignore everything that has to do with \*\*kargs.  Unless you're really curious, of course, in which case you should go ahead!
>
>I've included some tests below, which you can use to test your function to make sure it's working.  Just put your code and the tests in a file called "solution.py", and then run
```shell
    pytest -vv solution.py
```
>
>from the command line.
>
>I'll be back on Monday with a solution.
>
>Reuven

```python
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
```
