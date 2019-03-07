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
# 6. Repeat 1-5

def weather_info(weather_string):
    # input should be in following format:
    # YYYY-MM-DD, City, Country, high temperature, low temparature, amount of precipitation
    return

def collect_weather():
    # Prompt user for weather input until they enter blank
    while True:
        weatherInput = input("Enter weather data below, or blank to exit:\n" +
                             "Format: YYYY-MM-DD, City, Country, high temperature (in Celsius), " +
                             "low temparature (in Celsius), amount of precipitation (in mm)\n--> ")
        if weatherInput == "":
            print("Exiting program.")
            break
        print(weatherInput)

    return

collect_weather()
