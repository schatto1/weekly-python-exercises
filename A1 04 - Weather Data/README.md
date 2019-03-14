# Weather Data
This is my solution to Reuven Lerner's Weekly Python Exercise A1 Week 4 Exercise, `Weather Data`.

The prompt was to create a script that repeatedly prompts the user for weather information, and once splitting the string into a tuple, write the information to a file. The function loops until the user enters a blank entry into the prompt.

The information to be entered by the user would be in the following format:
- YYYY-MM-DD
- City
- Country
- High temperature (in Celsius)
- Low temperature (in Celsius)
- Amount of precipitation (in mm)

each separated by a comma (`,`).

## Getting Started

These instructions will get you a copy of the code on your local machine for further modification, development, and testing.

### Prerequisites

1. Python 3.
2. Installed "pytest" module in system.

### Installing

Download the file `weather_data.py` to a desired project location.

### Usage

1. Proceed to the desired project location in your terminal.
2. Run the function by entering "python3 weather_data.py".

## Original Prompt

Below, to quote Mr. Lerner:

>This week, we're going to start a new multi-week project, built out of several separate exercises. This time, we're going to deal with the weather. You know, the stuff that's outside, which you see between sessions on your computer.
>
>We're going to use this opportunity to learn more about a few subjects:
>- Getting and validating user inputs
>- Working with tuples
>- Writing information to files
>
>The idea is as follows: When the program is run, it'll ask the user to enter a weather report, containing the following pieces:
>- the date (in year-month-day format, e.g., 2019-02-12)
>- the city and country for the report
>- the high temperature
>- the low temperature
>- the amount of precipitation (i.e., rain or snow)
>
>This information will be input by the user into a single comma-separated string, as in:
```shell
2019-02-12, Tel Aviv, Israel, 15, 8, 3
```
>
>Note that I'm using degrees Celsius for the temperature (high and low), and millimeters to record the amount of precipitation.  If you live in a country that uses Fahrenheit and/or inches to measure precipitation, then you have my pity. And I'd suggest that you use metric units, if only to avoid dealing with floats when reading the data back from the disk (which we will eventually do).
>
>The user can enter as many such lines as they want.  When they enter a blank line, then the function returns, having written the data to disk.
>
>So the first task is to turn the user's input into a tuple containing 8 elements. You'll need to worry about spaces and the different types and formats of fields that we have -- including breaking the date into several parts.
>
>You will also want to make sure that you have the right number of elements, and you can (should) do some basic checking to ensure that they're of the right types.  It doesn't have to be a lot of checking, but at least something rudimentary.
>
>Then, when you've got the data you want, you'll write it to a file on disk, appending to whatever is there.  You should store the information as a (primitive) CSV-style file.  (Next week, we'll look at the "csv" module.  This week, you don't have to use anything that sophisticated.)
>
>This week, you'll need to read up on a few things:
>- The "input" function: https://docs.python.org/3/library/functions.html?highlight=len#input
>- The "str.split" method: https://python-reference.readthedocs.io/en/latest/docs/str/split.html
>- The "str.join" method: https://python-reference.readthedocs.io/en/latest/docs/str/join.html
>- The "str.isdigit" method: https://python-reference.readthedocs.io/en/latest/docs/str/isdigit.html
>- Using f-strings: https://realpython.com/python-f-strings/
>- Working with files: https://stackabuse.com/writing-files-using-python/
>I'm sorry, but I don't (yet) have tests for this week.  I'll try to post them in the forum in the coming day.
>
>Reuven
