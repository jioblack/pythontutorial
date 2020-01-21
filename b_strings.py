myString ="The boss is a bad guy"

#String slicing: stringName[start:stop:step]
print(myString[0:5])
print(myString[3:10:2])
print(myString[8:3:-1])
print(myString[-5:-2])
print(myString[-2::-2])

myString2 = "   The boss is a bad guy   "
print(myString2.strip())
print(myString2.rstrip())
print(myString2.lstrip())
#print(myString2.lstrip("T"))
#print(myString2.rstrip("guy"))
