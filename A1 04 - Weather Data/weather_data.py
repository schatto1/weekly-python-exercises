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

destinationFile = "weatherInfo.csv"

def collect_weather(outFile):

    with open(outFile, 'w') as output:
        # Prompt user for weather input until they enter blank
        while True:
            userInput = input("Enter weather data below, or blank to exit:\n" +
                                 "Format: YYYY-MM-DD, City, Country, high temperature (in Celsius), " +
                                 "low temparature (in Celsius), amount of precipitation (in mm)\n--> ").strip()
            if not userInput:
                print("Exiting program.")
                break

            if userInput.count(",") != 5:
                print(f"Input should have 6 comma-separated fields, not {userInput.count(',')}")
                continue

            date, city, country, hightemp, lowtemp, precip = userInput.split(",")

            if date.count("-") != 2:
                print(f"Date should be in YYYY-MM-DD format")
                continue

            year, month, day = date.split("-")

            year = year.strip()
            if not year.isdigit():
                print("Year should be numeric")
                continue

            month = month.strip()
            if not month.isdigit():
                print("Year should be numeric")
                continue

            day = day.strip()
            if not day.isdigit():
                print("Year should be numeric")
                continue

            city = city.strip()
            if not city:
                print("City was not entered")
                continue

            country = country.strip()
            if not country:
                print("Country was not entered")
                continue

            city = city.strip()
            if not city:
                print("City was not entered")
                continue

            hightemp = hightemp.strip()
            if not hightemp.isdigit():
                print("High temperature should be numeric")
                continue

            lowtemp = lowtemp.strip()
            if not lowtemp.isdigit():
                print("Low temperature should be numeric")
                continue

            precip = precip.strip()
            if not precip.isdigit():
                print("Precipitation should be numeric")
                continue

            weatherTuple = (year, month, day, city, country, hightemp, lowtemp, precip)

            output.write(f"{','.join(weatherTuple)}\n")
            print("Weather information written to file.")


    return

if __name__ == "__main__":
    collect_weather(destinationFile)
