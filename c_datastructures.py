#List
myList = [7,9,10,8.5,"The hue"]
print(myList)

#Tuples
myTuple = (3,5,6,7,10.9) #Immutable datastructure
print(myTuple)

#Dictionary
myDict = {1: "One", 2: "Two", 3: "Three"}
print(myDict)

#Sets
mySet = {2,3,4,5,6,7}
print(mySet)

#FrozenSets
myFrozenSet = frozenset(mySet) #Immutable unordered unique element datastructure
print(myFrozenSet)

#Range
myRange = range(1,10)

#Byte and ByteArray: Can hold values from 0 - 255
myByte = bytes([3,4,5,255]) #Immutable datastructure
print(myByte)

myByteArray = bytearray(10)
print(myByteArray)