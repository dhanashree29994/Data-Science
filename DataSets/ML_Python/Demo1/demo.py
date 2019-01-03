#KickStart
"""print("Hello World")
name = input("Enter Name ")
print(name)"""

#String declaration

name = "My Name is paul"
info = "I am David"
data = str("I am max")

print(name,info, data)

print(len(name))
print(type(name))

myinfo = r"My name is \n James"
print(myinfo)


#in for checking purpose
print("James" in myinfo)

#in for iteration
#it simply takes diff chars
for val in myinfo:
    print(val)

#print on same line
for val in "Dhanu":
    print(val,end="")
print(end="\n") 
#String add_function

#String is a collection of characters.
print(myinfo[0])
print(myinfo[0:])

print(myinfo.count("a"))
print(myinfo.index("a"))
Anilinfo = myinfo.replace("James", "Anil")
print(Anilinfo)
print(myinfo)
print(myinfo.capitalize())
print(myinfo.split(sep="a"))








