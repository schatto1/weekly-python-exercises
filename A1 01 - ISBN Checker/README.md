# ISBN Checker
This is my solution to Reuven Lerner's Weekly Python Exercise A1 Week 1 Exercise, `ISBNchecker`.

The prompt was to create a script that checks user input to see if it is a valid 13-digit ISBN. The last digit of a 13-digit ISBN is a "checksum", where the digit depends on the first 12 digits of the ISBN. Every other digit of the ISBN is multiplied by 3, with the first 12 digits summed together. This total is then divided by 10, and the remainder kept. This remainder is then subtracted from 10. If the resulting integer is identical to the checksum (the 13th digit), then the provided number is a valid ISBN.

This script performs the above operations on the user-provided number to see if the input is a valid ISBN.

## Getting Started

These instructions will get you a copy of the code on your local machine for further modification, development, and testing.

### Prerequisites

Python 3.

### Installing

Download the file `ISBNchecker.py` to a desired project location.

### Usage

1. Proceed to the desired project location in your terminal.
2. Start the script by entering `python3 ISBNchecker.py` into the command line.

## Original Prompt

Below, to quote Mr. Lerner:

>Welcome to Weekly Python Exercise, course A1!

>This course is designed to help you become more fluent in Python by doing exercises.  Every Tuesday, I'll send you a new problem (like this week).  I'll include some background information and reading that I hope will help you to understand how to get to the answer.  Through that reading and working on the exercise, you'll get better as a Python coder.

>An important part of WPE is also the forum.  People have used the forum in many different ways over the years, from sharing code (to compare and get feedback) to asking for help to finding people with whom they can pair-program in real time.  The forum isn't mandatory, but I very strongly encourage you to use it!  I know that programmers resist this thinking, but the more you discuss a problem, the better you'll understand it.

>This week, we'll start off by calculating checksums.  And we'll do it with an algorithm near and dear to my heart, calculating the checksum for ISBN-13.

>Along the way, we'll practice:
> - Getting input from the user
> - Converting data from strings to integers (and back)
> - Iterating with "for" loops
> - Using the "enumerate" method
> - Some basic math operations, including % (modulus)

>You see, every book published in the world has (or should have) a unique ISBN (international standard book number).  This allows everyone from publishers to bookstores to keep track of all of the books out there, even if different books have the same name. If you have experience with databases, you can think of ISBNs as the primary key of the book world.

>For example: On my desk, I have a book called "Artificial Unintelligence," by Meredith Broussard, which I recently started to read, and which is quite fascinating.  But we'll ignore the content right now, and concentrate on its ISBN-13, which is 978-0262038003.

>The thing is, an ISBN-13 isn't just a serial number. The final digit is a "checksum," meaning that it helps to ensure that the previous digits weren't entered incorrectly.  If someone were to enter 978-0262038002 (notice that there's a 2 at the end, rather than a 3), then we would know that the ISBN-13 was impossible, and thus incorrect.

>How is the checksum digit calculated? Through a pretty simple algorithm: We take the first 12 digits, and multiply each one by either 1 or 3, alternating between them.  We then take the sum and divide it by 10, taking the remainder. That remainder will be a digit between 0 and 9.  We subtract the remainder from 10, and *that's* the final digit.

>In other words, if we take my book's ISBN-13:

>`978-0262038003`

>Let's go through the first 12 digits:

>`978026203800`

>We now multiply each digit by either 1 or 3, starting with 1, and alternating between them:

>`9 + 3*7 + 8 + 3*0 + 2 + 3*6 + 2 + 3*0 + 3 + 3*8 + 0 + 3*0`

>The total is 87.  We can then divide this by 10, getting a remainder of 7.  10 - 7 = 3, and sure enough, 3 should be the final digit.

>For this week, your exercise is to ask the user to enter an ISBN, and to indicate whether it is valid or not.  For example:
```shell
Enter an ISBN: 9780262038003
Yes, valid
Enter an ISBN: 9780262038002
No, invalid
```

>From my perspective, it's enough to get input containing only digits.  If you want to remove and/or ignore non-digit characters, that's totally fine.

>If you already have a good idea of how to do this, then great!  If not, then here are some resources you can use:
> - The "input" function: https://docs.python.org/3/library/functions.html?highlight=len#input
> - Converting strings to ints: https://guide.freecodecamp.org/python/how-to-convert-strings-into-integers-in-python/
> - The "enumerate" method: https://docs.python.org/3/library/functions.html?#enumerate
> - The "str.isdigit" method: https://python-reference.readthedocs.io/en/latest/docs/str/isdigit.html
> - Displaying output with f-strings: https://realpython.com/python-f-strings/
> - Modulus: https://python-reference.readthedocs.io/en/latest/docs/operators/modulus.html

>And if you're interested, you can also learn more about ISBN-13:
- https://en.wikipedia.org/wiki/International_Standard_Book_Number#ISBN-13_check_digit_calculation

>I'll be back on Monday with my suggested solution.  Meanwhile, discuss your ideas (and frustrations) with others in the forum!  And when you post code, don't forget to hide it using the "greek" option, so that others don't accidentally see your code.
