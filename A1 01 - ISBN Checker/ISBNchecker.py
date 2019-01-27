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

# Prompt user for ISBN number, keep only numeric digits
isbn_string = re.sub(r"\D", "", input('Enter the ISBN number: '))

print(isbn_string)
