# Import all necessary packages
# import re #regex package

# Pseudocode:
# 1. Prompt user for string
# 2. If string is blank, exit program
# 3. Split string into 8 parts:
    # 1. Year (string)
    # 2. Month (string)
    # 3. Day (string)
    # 4. City (string)
    # 5. Country (string)
    # 6. High temp (int)
    # 7. Low temp (int)
    # 8. Precipitation (int)
# 4. If cannot split into 8 parts, tell user, return to loop
# 5. Save parts into tuple containing 8 elements
# 6. Write tuple onto file
# 7. Repeat 1-6

def weather_string_to_tuple(weatherString):
    '''
    Checks the user input to see if there is the required
    number of inputs, and if the inputs are of the desired
    type. Returns a tuple containing weather information extracted
    from user provided input.

    Input should be in following format:
    YYYY-MM-DD, City, Country, high temperature, low temparature, amount of precipitation
    '''

    passedChecks = True

    if weatherString.count(",") != 5:
        print(f"Input should contain 6 comma-separated fields, not {weatherString.count(",")}")

    weatherData = weatherString.split(",")
    weatherData = [item.strip() for item in weatherData]

    if weatherData[0].count("-") != 2:
        print(f"Date should be in YYYY-MM-DD format")
        passedChecks = False

    dateFields = weatherData[0].split("-")

    if not dateFields[0].isdigit():
        print("Year should be numeric")
        passedChecks = False

    if not dateFields[1].isdigit():
        print("Month should be numeric")
        passedChecks = False

    if not dateFields[2].isdigit():
        print("Day should be numeric")
        passedChecks = False


    weatherTuple = tuple(dateFields + weatherData[1:])

    return weatherTuple, passedChecks

    if s.count(',') != 5:
                print(f"Expected 6 comma-separated fields; you gave {s.count(',')}")
                continue

            date, city, country, hightemp, lowtemp, precip = s.split(',')

            if date.count('-') != 2:
                print(f"Expected date in year-month-day format")
                continue

            year, month, day = date.split('-')

            year = year.strip()
            if not year.isdigit():
                print("Year isn't numeric")
                continue

            month = month.strip()
            if not month.isdigit():
                print("Month isn't numeric")
                continue

            day = day.strip()
            if not day.isdigit():
                print("Day isn't numeric")
                continue

            city = city.strip()
            if not city:
                print("City is empty")
                continue

            country = country.strip()
            if not country:
                print("Country is empty")
                continue

            hightemp = hightemp.strip()
            if not hightemp.isdigit():
                print("High temp isn't numeric")
                continue

            lowtemp = lowtemp.strip()
            if not lowtemp.isdigit():
                print("Low temp isn't numeric")
                continue

            precip = precip.strip()
            if not precip.isdigit():
                print("Precip isn't numeric")
                continue

            t = (year, month, day, city, country, hightemp, lowtemp, precip)

def collect_weather(outFile):

    with open(filename, 'w') as f:
        # Prompt user for weather input until they enter blank
        while True:
            userInput = input("Enter weather data below, or blank to exit:\n" +
                                 "Format: YYYY-MM-DD, City, Country, high temperature (in Celsius), " +
                                 "low temparature (in Celsius), amount of precipitation (in mm)\n--> ").strip()
            if not userInput:
                print("Exiting program.")
                break
            weather_string_to_tuple(userInput)

    return

destinationFile = "weatherInfo.csv"
collect_weather(destinationFile)
