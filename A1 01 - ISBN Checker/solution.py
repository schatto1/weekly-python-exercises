#!/usr/bin/env python3

# Get the ISBN from the user
user_isbn = input("Enter an ISBN-13: ").strip()

isbn = ''

# Only capture digits from the user's input
for one_digit in user_isbn:
    if one_digit.isdigit():
        isbn += one_digit
check_digit = isbn[-1]
print(f"Checking '{isbn}', check digit {check_digit}")

is_valid = False

# Calculate the checksum
if len(isbn) == 13:
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

if is_valid:
    print("Your ISBN is valid")
else:
    print("Your ISBN is invalid")
