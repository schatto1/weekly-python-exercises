# Multiple line file reader
This repository contains my solution to Reuven Lerner's Weekly Python Exercise Sample Exercise #1, ```read_n```.

The prompt was to create a generator function that takes two arguments — the filename from which to read, and the maximum number of lines that should be returned with each iteration.

## Getting Started

These instructions will get you a copy of the code on your local machine for further modification, development, and testing.

### Prerequisites

Python 3.

### Installing

Download the file ```read_n.py``` to a desired project location.

### Usage

1. Once in your desired project location, start the Python interpreter.
2. Import the module by typing ```import read_n```.
3. Call the function with ```read_n.read_n(filename, number of lines to read)```.

### Original Prompt

Below, to quote Mr. Lerner:

>Welcome to the first sample exercise!  If you subscribe to Weekly Python Exercise, you'll get a new exercise like this one sent to you automatically every Tuesday.  Moreover, you'll have exclusive access to our forums and discussion.

>Normally, if we want to read from a file in Python, we do so one line at a time, as follows:
```python
    for one_line in open(filename):
        print(one_line.rstrip())
```
>But sometimes, we want to read more than one line at a time.

>For example, suppose a logfile is written in a three-line format. Reading one line at a time is pretty useless, especially if we want to compare a value on line 1 with a value on line 3.

>Reading the entire file into a string isn't what we want, either; it might well be too long for us to read the entire thing.  What I really want to do is read three lines at a time.

>For this exercise, I want you to write a generator function that takes two arguments — the filename from which to read, and the maximum number of lines that should be returned with each iteration.  That is, if our file is
```python
    File line 0 aaa
    File line 1 bbb
    File line 2 ccc
    File line 3 ddd
    File line 4 eee
    File line 5 fff
    File line 6 ggg
```
>Then I could do this:
```python
    for two_lines in read_n(filename, 2):
        print(two_lines.rstrip())
```
>And the result would be:
```python
   File line 0 aaa
   File line 1 bbb

   File line 2 ccc
   File line 3 ddd

   File line 4 eee
   File line 5 fff

   File line 6 ggg
```
>Notice that the last line is by itself, because there was an odd number of lines.  We could also say:
```python
    for four_lines in read_n(filename, 4):
        print(four_lines.rstrip())
```
>This time we get four lines at a time:
```python
   File line 0 aaa
   File line 1 bbb
   File line 2 ccc
   File line 3 ddd

   File line 4 eee
   File line 5 fff
   File line 6 ggg
```
>With each iteration, read_n should return a string (not a list) containing up to the number of lines specified by the second parameter.

>Note that read_n isn't a function that returns a list, but rather a generator function.  In other words, executing read_n will return a generator object -- in other words, an object that implements Python's iteration protocol, and thus knows how to behave inside of a "for" loop or list comprehension.

>If you're not sure how to write a generator function, here is some good online documentation here:

>    https://realpython.com/blog/python/introduction-to-python-generators/

>I'll be back tomorrow with a solution.