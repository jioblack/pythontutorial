"""
Time in python can be manipulated using the 'time' module.
Data and time can be manipulated using the 'datetime' module.

In computer systems, we have the concept of an 'epoch'.
This is the time in seconds since Jan 1st, 1970.

From the 'time' module we have the ctime() method to calculate
current time with epoch

"""
import time
import datetime

epoch = time.time()
print(epoch)

currentTime = time.ctime(epoch)
print(currentTime)

today = datetime.datetime.today()
print("Today's date is: {}/{}/{}".format(today.day, today.month, today.year))
print("Current time is: {}:{}:{}".format(today.hour, today.minute, today.second))

"""
One can also combine a date object and a time object to form a
datetime object.
"""
from datetime import date, time, datetime
import time as tim

d = date(month=3,year=2020, day=6) #Creates a date object
t = time(minute=45, hour=2, second=18) #Creates a time object

#Sleep/Freeze the execution of your program/script using sleep() method from
#the time module
tim.sleep(4)
dt = datetime.combine(d,t)

print(dt)

"""
Sorting Date Object using list Object.
This involves adding the date object inside the list and call the sort method of
the list.

The performance of a program/script (i.e. the execution time) can be calculated
using the perf_counter() method from the 'time' module. To accomplish this put
it as the beginning and end of your code, the subtract and the difference is your
execution time.
e.g.
    startTime = time.perf_counter()
    
    ====your code goes here====

    endTime = time.perf.counter()

    executionTime = endTime - startTime
"""

