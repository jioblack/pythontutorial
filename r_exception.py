"""
    Exceptions can be handled using try, except, else, assert and finally statements.
"""
try:
    # Code to test for exception
    a, b = [float(x) for x in input("Enter two numbers:").split()]
    c = a / b
    print(c)
except:
    print("I will run if an exception is raised")
    print("Division by zero not allowed")
    print("Your second number (denominator) can't be zero")
else:
    print("I will run if there is no exception raised")
finally:
    print(
        "I must run weather you like it or not. Even if an exception should happen I wont be stopped "
    )
""" 
import logging

logging.basicConfig(filename=mylog.log, level=logging.DEBUG)
logging.critical("Critical")
logging.error("Error")
logging.warn("Warning")
logging.info("Information")
logging.debug("Debugging")

Note: The log level i.e. level=logging.xxxx determines which logging type is shown. log level ERROR show Error logs above (i.e. error and critical)
      log level DEBUG shows all logs from Debug to Critical

"""

#Assertion can also be used to handle errors. The example below shows how
even = int(input("Enter an even number:"))
#If the input value does not satisfy the assert i.e. if it isn't even, an AssertError is raised
assert even % 2 == 0, print(
    "You entered an odd number, you need to enter an even number")

#Tip: You can wrap the assertion using a try except block for better error handling
try:
    even = int(input("Enter an odd number:"))
    assert even % 2 != 0, print(
        "You entered an even number, you need to enter an odd number")

except AssertionError as output:
    print(output)