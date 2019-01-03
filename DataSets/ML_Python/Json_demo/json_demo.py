emp ='{"id":"101", "Name":"Sam", "Age":"33"}'
import json

data = json.loads(emp)#returns a dictionary
print(data)
print(type(data))

for k,v in data.items():
    print(k,v)



fp = open("data.json", "r")
data2 = json.load(fp)
print(type(data2))
for k,v in data2.items():
    print(k,v)



import os
os.mkdir("Myfolder")
#os.remove("Myfolder")


