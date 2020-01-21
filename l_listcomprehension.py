"""
List Comprehension are used in creating new list from iterables/another list

syntax:
    new_list = [expression for item in iterable if condition]

    new_list = [expression for loop one or more condition]
"""
#Example of list comprehension

number = [2, 3, 4, 5, 6, 7, 8, 9, 10]

square_list = [n * n for n in number]
print(square_list)

even_list = [n for n in number if n % 2 == 0]
print(even_list)

#Multiplying two list using list comprehension
one = [2, 4, 5, 7, 9]
two = [3, 12, 20, 31, 27]

multi_list = [one[i] * two[i] for i in range(len(one))]
print(multi_list)
"""
Using for loop this can be achieved as thus:

    result=[]
    for i in one:
        for i in two:
            result.append(one[i] * two[i])
"""

#Display list elements common in two list
three = [2, 5, 7, 12, 3]
four = [3, 8, 7, 12, 4]

common = [i for i in three if i in four]
print(common)
"""
Using for loop and if statement this can be achieved as thus:

    result=[]
    for i in three:
        if i in four:
            result.append(i)
"""