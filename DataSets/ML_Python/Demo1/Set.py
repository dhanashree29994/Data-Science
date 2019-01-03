#unique values
#scattered format
#unordered output
#not sequential in memory


myset = {10,30,450,10}
print(myset)

print(type(myset))

#Add operation
myset.add(300)
print(myset)

print(300 in myset)

#remove
myset.remove(30)
print(myset)

set1 = {10,20,30,40}
set2 =  {20,40,10,100}

#Union

print(set1.union(set2))

#Intersection

print(set1.intersection(set2))

#Difference
print(set1.difference(set2))

#symmetric difference
print(set1.symmetric_difference(set2))


#Superset subset 
print(set1.issuperset(set2))

print(set2.issubset(set1))



