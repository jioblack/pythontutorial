#Take inputs from users
f = input("Enter a name ")
print(f)

#Take multiple inputs: The input value is splitted with space and assigned to x, y, z
x,y,z = input("Enter your first middle and last name separated with space ").split()
print("Welcome ", x ,y ,z)

#print formatting %d=decimal %f=float %s=string %c=character
a = 7
b = 8.7
c = "Hello"
d = 'A'

print("The values are %d %f %s %c" %(a ,b ,c ,d))