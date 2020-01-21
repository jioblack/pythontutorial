"""
    Learn how to create a custom module
    A module is a normal python script which is imported into the
    current running script.
    For example we would import our g_function.py file and invoke the
    times2() and times3() function.

"""
import g_functions as gfs

print(gfs.times2(5))
print(gfs.times3(5))
print(gfs.times3(21))
