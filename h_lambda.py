#Lambda functions are defined with the "lambda" keyword
#Lambda functions don't need a "return" statement
lamb = lambda x: x**2
print(lamb(4))

f = lambda x: "Yes" if x % 2 == 0 else "No"
print(f(4))

pie = lambda a, b, c: a * b * c
print(pie(4, 2, 5))

#Using filter, map and reduce functions

#filter function usage
lst = [10, 2, 5, 6, 7, 8, 9, 35, 21, 5, 7]
fill = filter(lambda x: x % 2 == 0, lst)  #Returns a filter object
'''for i in fill:
    print(i)'''
fillList = list(fill)  #Converts filter object to a list
print(fillList)

#map function usage
mill = map(lambda x: x**2, lst)  #Returns a map object
"""for i in mill:
    print(i)"""

millList = list(mill)  #Converts map object to a list
print(millList)

#reduce function usage
#To use 'reduce' function, it must first be imported from 'functools' module
from functools import reduce

#Calculates the sum of a list by adding the each element (two at a time) in the list
rill = reduce(lambda x, y: x + y, lst)  #Retruns an integer
print(rill)