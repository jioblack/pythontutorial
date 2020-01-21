"""
Generators are functions that return a sequence of values back.
A generator function is returned like any other function but makes use
of the 'yield' keyword when doing so.

"""


def myGenerator(x, y):
    while x <= y:
        yield x
        x += 1


result = myGenerator(1, 20)  #Gives a generator object
print(result)

for i in result:
    print(i)