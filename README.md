# Perl-like Sliceable Dict class for Python
This repository contains my solution to Reuven Lerner's Weekly Python Exercise Sample Exercise #2, ```Sliceable dict```.

The prompt was to inherit the built-in Python "dict" class and construct a "sliceable dict" class, which returns a list of values when it receives a sequence within square brackets and the sequence is not a key.

Below, to quote Mr. Lerner:

>Welcome to the second sample exercise!  If you subscribe to Weekly Python Exercise, you'll get a new exercise like this one sent to you automatically every Tuesday.  Moreover, you'll have exclusive access to our forums and discussion.

>For many years, I worked with the Perl language. During those years, Perl and Python were competing for mindshare among developers; in the end, Python has come out *way* ahead.  Today, Perl is mostly a legacy language, although there remains some hope among its users that Perl 6 will somehow become popular.

>Today, I prefer Python -- but there are some things that I really enjoyed in Perl that Python still doesn't support. One of those was the idea of a "dict slice."  That is, we know that I can create a dict:
```python
    d = {'a':1, 'b':2, 'c':3}
```
>and I can obviously retrieve an element from it:
```python
    d['a']
```
>Wouldn't it be nice to retrieve more than one element, and get back a list of values?  For example:
```python
    print(d[['a', 'b']])    # returns [1,2]
```
>Pandas actually supports something like this on its Series and DataFrame classes.  But it would be nice to have on a dict.

>This assignment is to create a SliceableDict class. The idea is that it works just like a regular dictionary, except that if it gets a sequence in the square brackets, and if the sequence isn't a key, then we get back a list of values.

>For example:
```python
    d = SliceableDict(a=1, b=2, c=3, ac=4)

    print(d['a'])        # 1
    print(d['b'])        # 2
    print(d['c'])        # 3
    print(d[('b', 'c')]) # [2,3]
    print(d['bc'])       # [2,3]
    print(d['ac'])       # 4
```
>Two hints to help you out:
>* You'll want your class to inherit from the built-in "dict" class, and
>* You'll want to implement the __getitem__ method

>I'll be back tomorrow with the solution.