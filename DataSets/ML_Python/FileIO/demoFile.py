"""fp = open("data")
ans = fp.read(2)
print(ans)
print(type(ans))





fp.seek(0)
for val in fp.readlines():
    print(val, end="")



"""
"""Modes in FILE I/O 
r-->iff NA create
w-->
a--> create iff not available
"""
"""fw  = open("newfile.txt", "a+")
fw.write("\n My name is sam")
fw.write("\n I am from Mumbai")
fw.write("\n I play Football")

fw.seek(0)
print(fw.read())"""




fw = open("mydata.csv", "w")
fw.write("ID, name , age")
fw.write("\n101, Sam, 44")
fw.write("\n102, jam, 55")
fw.write("\n103, Ram,66")

print("CSV Created")
