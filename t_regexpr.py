""" A regular expression, regex or regexp is a sequence of character that defines a search pattern.
    Usually such patterns are used by string searching algorithms for 'find' or 'find and replace'
    operations on strings, or for input validation.
    The 're' module in python is used to perform regular expression. The module contain
    methods such as: match(), search(), findall(), split() and sub().
    Regular Expression can be made up of Sequence, Anchors, special characters and quantifiers.
    Each sequence and anchor character starts with a backslash.

    Sequence characters represent a single character in a string. e.g.

    1. \d ===> This stands for any digit [0-9].
    2. \D ===> This represents the opposite of \d i.e. any non digit character.
    3. \s ===> This represents a whitespace in a string (spaces, tabs & newline)
    4. \S ===> Represents a no whitespace
    5. \w ===> Represents any alphanumeric character i.e. letters or numbers.
    6. \W ===> Opposite of \w

Anchor Chracters: Don't actually match characters but position before or after a string. e.g.

    7. \b ===> Around a word (Word boundary)
    8. \B ===> Not a word boundary
    8. \A or ^ ===> Matches only at the start of a string
    9. \Z or $ ===> Matches only at the end of the string
"""

import re

string = "The boy is a good boy, and he likes ben 10"

#Lets search the string for the first word that starts with b and contains three letters.
oneword = re.search(r'b\w\w', string)
print(oneword.group())

#Lets search the string and return all the words that starts with b and contains three letters.
allword = re.findall(r'b\w\w', string)
print(allword)

#Lets search the string and return the word that starts with b and contains three letters, only
#if it is at the beginning
matchword = re.match(r'T\w\w', string)
print(matchword.group())

#Split a string at the point the regular expression is matched
splitword = re.split(r'b\w\w', string)
print(splitword)

#Replace the matching regular expression with a new string e.g. 'girl' or a regular expression.
splitword = re.sub(r'b\w\w', 'girl', string)
print(splitword)
"""
    Quantifiers are used to match multiple characters in a regular expression.
    e.g.
    + ===> Specifies 1 or more characters to match e.g. \d+ means 1 or more digits

    * ===> Specifies 0 or more characters to match e.g. \d* means 0 or more digits

    ? ===> Specifies 0 or 1 characters to match e.g. \w? means 0 or 1 alphanumeric character

    {2} ===> Specifies exactly number of occurrences (in curly braces) to match. 

    {2,4} ===> Specifies range of numbers (minimum and maximum) occurrences in the regular expression.
"""

oneORmore = re.findall(r'b\w+', string)
print(oneORmore)

zeroORmore = re.findall(r'b\w*', string)
print(zeroORmore)

zeroORone = re.findall(r'b\w?', string)
print(zeroORone)

exactlyTwo = re.findall(r'b\w{2}', string)
print(exactlyTwo)

Zero_One = re.findall(r'b\w{0,1}', string)
print(Zero_One)

#Examples matching dates
datestring = "The day I met you was 3-4-2010 funny it was virtual and have lasted till now 04-2-2020"
ourdate = re.findall(r'\d{1,2}-\d{1,2}-\d{4}', datestring)
print(ourdate)
"""
    Special Characters:
        \ ===> Escape

        . ===> Matches any character except a new line

        ^ ===> Match only at the beginning of a string

        $ ===> Match only at the end of a string

        [...] ===> Matches only characters or the range of characters provided (i.e character set)  
                    e.g. [aef] or [a-d] or [A-E] 

        [^...] ===> Matches all characters except those provided in the range. e.g. [^a-f]

        (...) ===> Match a regular expression within the provided brackets.

        (A | B) ===> Match any of the provided regular expressions A or B

"""
oneword = re.findall(r'\b[a-h]\w+', string)
print(oneword)