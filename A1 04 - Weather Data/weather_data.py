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

def collect_weather(outFile):

    with open(outFile, 'w') as f:
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
