"""
    Reading/Writing files in python either text files or binary (images, audio,video) files can be done 
    using open() function.
        f=open('filename', 'mode','optional buffer').
        filename = file to be read
        mode = read(r), write(w), append (a), writeNread (w+), readNwriteNappend(r+), appendNread(a+), 
               exclusive(x):Creates a new file.
               For binary files and a 'b' to the end of each mode above e.g. rb, wb, ab, w+b, r+b, a+b, xb
        buffer = default 4096 or 8096
        f.close()
"""
#Writing from a file
f=open("x_myfile.txt","w")
string = input("Enter your comment here:")
f.write(string)
f.close()

#Reading from a file
f1=open("x_myfile.txt","r")
str1=f1.read(-1)
print(str1)
f1.close()

#Writing multiline strings and checking if file exist
import os, sys
if os.path.isfile("x_mymultifile.txt"): #Checks if file exist
    f=open("x_mymultifile.txt","w")
    print("Enter your comment here(Type & when done):")
    str2 =""
    while str2 !="&":
        str2=input()
        f.write(str2+"\n")
    f.close()
else:
    sys.exit("File Not Found")

"""
    Python Pickel module can be used to perform data serialization.
"""
import pickle

class Student:
    def __init__(self,id,name,score):
        self.id=id
        self.name=name
        self.score=score

    def display(self):
        print(self.id, self.name, self.score)



f=open("x_serialized.dat","wb") #Creates file that serialized data would be stored
s=Student(1,"Nora", 85) #Data to be stored
pickle.dump(s,f) #Serializing the data
f.close()

r = open("x_serialized.dat","rb") #Read in serialized data
obj=pickle.load(r) #Load the serialized data
r.close()

obj.display() #Display the content from the serialized data