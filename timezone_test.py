## This was used to test get_time_of_day
## Originally a function in src/utilities.py it has been turned into a class method in the Company class

from src.utilities import (
    get_time_of_day
)

timezones = ['US/Pacific', 'US/Central', 'US/Eastern']

for timezone in timezones:
    print(get_time_of_day(timezone))