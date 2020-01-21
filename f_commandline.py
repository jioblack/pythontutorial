'''Passing commandline argument in python involves
    importing the "sys" module and accessing the "argv"
    list. This list contains value passed through commadline'''

import sys

cmdLst = sys.argv

for i in cmdLst:
    print(i)

#Run script python commandline.py arguments