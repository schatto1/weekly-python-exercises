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

# Start program, let user know what will happen
print(f"Welcome to the ISBN Checker. Please enter the ISBN number to check, or q to quit.")

while True:
    # Prompt user for ISBN number, keep only numeric digits
    isbn_string = input('Enter the ISBN number: ')

    if isbn_string == "q":
        print(f"Exiting program...")
        quit()

    # Strip string of all non-numeric chars
    isbn_string = re.sub(r"\D", "", isbn_string)

    # Reprompt if not 13 digits
    if len(isbn_string) != 13:
        print(f"Your input only contains {len(isbn_string)} digits. Please enter a 13 digit ISBN number.")

    # got 13 digits, keep going with program
    else:
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
            print(f"Yes, {isbn_string} is a valid ISBN number.")
        else:
            print(f"No, {isbn_string} is NOT a valid ISBN number.")
