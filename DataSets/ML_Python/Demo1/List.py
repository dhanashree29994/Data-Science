#List in python.Dynamic collection in which you can add remove etc as required.
#Mutable 
#Allows duplicates

mylist = [10,20,30,40,50]
print(mylist)
print(type(mylist))

mylist2 = list([2,3,4,5])
print(mylist2)

#Append
print(mylist.append("Last"))
print(mylist) 


#insert works on index
mylist.insert(0,1)
print(mylist)


#WAYS TO DELETE
#Remove works on value and removes the first value

mylist.remove(40)
print(mylist)

#Pop works on index

mylist.pop(0)
print(mylist)


#No replace --> directly reassignment
mylist[0]=555
print(mylist)

#Reverse -->
mylist.reverse()
print(mylist)
print(len(mylist))

print(10 in mylist)

#Sorting a list
l3 = [10,20,30,40,50,90,2,1,5]
l3.sort( reverse = True)
print(l3)

#Min - max

print(max(l3))
print(sum(l3))

#Nested list to access inner elements use nested for loops

l4 = [[1,2,3],[4,5,6],[7,8,9]]

for i in l4:
    for j in i:
        print(j)


