# Import all necessary packages
# import re #regex package

def weather_info(weather_string):
    # input should be in following format:
    # YYYY-MM-DD, City, Country, high temperature, low temparature, amount of precipitation

    # Strip string of all non-numeric chars
    isbn_string = re.sub(r"\D", "", isbn_string)

    # Throw exception if not 13 digits
    if len(isbn_string) != 13:
        return f"bad length of {len(isbn_string)}"

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

def validate_isbns(filename, *args):
    # open file to append to using first argument
    with open(filename, "a") as output:
        for isbn in args:
            output.write(isbn + "\t" + str(check_isbn(isbn)) + "\n")

    print("Report has been created.")
    return
