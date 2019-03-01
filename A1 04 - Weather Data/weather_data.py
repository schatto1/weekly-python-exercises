# Import all necessary packages
# import re #regex package

def weather_info(weather_string):
    # input should be in following format:
    # YYYY-MM-DD, City, Country, high temperature, low temparature, amount of precipitation
    return

def collect_weather():
    # Prompt user for weather input until they enter blank
    while True:
        weatherInput = input("Enter weather data below, or blank to exit:\n" +
                             "(Format: YYYY-MM-DD, City, Country, high temperature, " +
                             "low temparature, amount of precipitation)\n--> ")
        if weatherInput == "":
            print("Exiting program.")
            break
        print(weatherInput)

    return

collect_weather()
