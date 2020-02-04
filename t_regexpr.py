""" A regular expression, regex or regexp is a sequence of character that defines a search pattern.
    Usually such patterns are used by string searching algorithms for 'find' or 'find and replace'
    operations on strings, or for input validation.
    The 're' module in python is used to perform regular expression. The module contain
    methods such as: match(), search(), findall(), split() and sub().
    Regular Expression are made up of Sequence characters. Each character starts with a backslash.

    1. \d ===> This stands for any digit [0-9]. It matches a single character in a string.
    2. \D ===> This represents the opposite of \d i.e. any non digit character.
    3. \s ===> This represents a whitespace in a string
    4. \S ===> Represents a no whitespace
    5. \w ===> Represents any alphanumeric character i.e. letters or numbers.
    6. \W ===> Opposite of \w
    7. \b ===> Around a word
    8. \A ===> Matches only at the start of a string
    9. \Z ===> Matches only at the end of the string
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
    + ===> Specifies one or more repetition of the preceding regular expression. e.g. '\d+' means
            one or more digits.

    * ===> Specifies zero or more repetition of the preceding regular expression e.g. '\d*' means
            zero or more digits.

    ? ===> Specifies zero or one repetition of the preceding regular expression

    {2} ===> Specifies exactly two occurrences of the preceding regular expression. You can change
                the number within the curly brackets.

    {2,4} ===> Specifies minimum of two and maximum of 4 occurrences in the regular expression.
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

        [...] ===> Provides a range of value e.g. [a-d] or [A-E]

        [^...] ===> Matches all characters except those provided in the range. e.g. [^a-f]

        (...) ===> Match a regular expression within the provided brackets.

        (A | B) ===> Match any of the provided regular expressions A or B

"""
oneword = re.findall(r'[a-z]\w{2,5}', string)
print(oneword)