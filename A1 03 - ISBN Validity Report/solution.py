#!/usr/bin/env python3

def validate_isbns(filename, *args):
    with open(filename, 'w') as outfile:

        for user_isbn in args:

            isbn = ''

            for one_digit in user_isbn:
                if one_digit.isdigit():
                    isbn += one_digit
                    check_digit = isbn[-1]

            is_valid = False

            if len(isbn) != 13:
                outfile.write(f'{isbn}\tbad length of {len(isbn)}\n')
                continue

            total = 0
            for index, digit in enumerate(isbn[:12]):

                if index % 2:               # odd index? 3*digit
                    total += 3 * int(digit)
                else:
                    total += int(digit)

            user_check_digit = 10 - (total % 10)
            if user_check_digit == 10:
                user_check_digit = 0

            if user_check_digit == int(check_digit):
                is_valid = True


            outfile.write(f'{isbn}\t{is_valid}\n')


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
