# ISBN Checker
This is my solution to Reuven Lerner's Weekly Python Exercise A1 Week 2 Exercise, `ISBNcheckerFunction`.

The prompt was to create a script containing a function `validate_isbn` that checks user input to see if it is a valid 13-digit ISBN. The last digit of a 13-digit ISBN is a "checksum", where the digit depends on the first 12 digits of the ISBN. Every other digit of the ISBN is multiplied by 3, with the first 12 digits summed together. This total is then divided by 10, and the remainder kept. This remainder is then subtracted from 10. If the resulting integer is identical to the checksum (the 13th digit), then the provided number is a valid ISBN.

The `validate_isbn` function performs the above operations on the user-provided number to see if the input is a valid ISBN.

## Getting Started

These instructions will get you a copy of the code on your local machine for further modification, development, and testing.

### Prerequisites

1. Python 3.
2. Installed "pytest" module in system.

### Installing

Download the file `validate_isbn.py` to a desired project location.

### Usage

1. Proceed to the desired project location in your terminal.
2. Test the function by entering "pytest validate_isbn.py".

## Original Prompt

Below, to quote Mr. Lerner:

>Last week, we looked at how we could write a program to check for valid ISBN-13 numbers.  We're going to expand on this in a few ways this week:
> - We're going to rewrite our checker as a function, rather than a standalone program
> - We're going to have our function raise an exception if it gets input that isn't valid
> - We're going to specify our function's behavior with "pytest"
>If you already wrote last week's program using a function, then you're ahead of the game!
>
>Each of these ideas is important in programming in general, and in Python in particular.  So even if you might think we're just repackaging what we did before, I hope that you'll appreciate the importance of the ideas.  Besides, you'll probably have some logistical issues starting to get things going, and I want you to have some time to resolve those.
>
>First: Last time, we asked the user for input, and then fed that input to our ISBN-checking algorithm.  This time, the idea is to write a function called "validate_isbn", which will return a "True" or "False" value.  (Note: The function won't print anything.  It'll return a value, which can then be printed by whoever calls the function.)  The input to the function should be a string, and that string can contain any number of characters.  We'll ignore the non-numeric characters; if 13 numeric characters remain, then we'll return "True" or "False" to indicate whether the ISBN is valid.
>
>Second: If we receive too few or too many digits, then we'll raise a `TypeError` exception.  (It's normally not a good idea to raise built-in Python exceptions, but I don't want to add too much stuff to this exercise.)
>
>Third: While my prose is undoubtedly as precise as it is briliant, automated tests are a far better way to specify behavior. An increasingly popular system for testing software in Python is known as "pytest".  You can download and install "pytest" with
    ```shell
    pip3 install pytest
    ```
>
>I must admit that I've fallen in love with "pytest" in the last 6-8 months, and have been using it more and more in my teaching and in my own work. For now, we'll write our tests in the same file as we define our solution. I generally use a file called "solution.py" for this, which means that I can run the tests as:
    ```shell
    pytest solution.py
    ```
>
>This tells "pytest" that it should open the file "solution.py" (in the current directory), and run all of the tests in it.  Tests are functions whose names start with the pattern "test_".  Normally, we won't really want to put our tests in the same file as our function, but for now, it's not a terrible thing.
>
>If all of the tests pass (i.e., are green), then you can be pretty sure that the function works correctly.  Or if nothing else, you can be sure that the more standard cases are working.
>
>While it's easy to get into "pytest", it's also easy to get deep into testing, and to use some obscure features. I'm going to try to use very few "pytest" features this week, slowly but surely using more of them as the course progresses.  Actually, I will be using one powerful "pytest" feature already, namely the use of "parametrized" tests -- which let you define a number of inputs and the outputs you expect from similar tests.  I hope that it won't make the tests too confusing to read, understand, or use.
>
>Here are some resources to read up on this week's exercise:
> - Defining functions: https://anh.cs.luc.edu/python/hands-on/3.1/handsonHtml/functions.html
> - Installing "pytest": https://docs.pytest.org/en/latest/getting-started.html
> - Using "pytest": https://docs.pytest.org/en/latest/getting-started.html
> - Raising exceptions: https://realpython.com/python-exceptions/#raising-an-exception
>Questions or comments?  (Or problems getting this set up?)  Ask away in the forum!
>
>Meanwhile, I'll be back with a solution on Monday.

```python
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
```
