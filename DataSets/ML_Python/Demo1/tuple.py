#Tuple read only data structure
#Allows duplicates so count
#Allows indexing so index() is also there.

mytup = (10,30,"Sam",33,10)
print(mytup)
print(type(mytup))


print((30 in mytup))

for val in mytup:
    print(val)

print(mytup[0:2])




tl = list(mytup)
print(tl)

lt = tuple(tl)
print(lt)


#mostly used for db ops
mytup1 = (1,)
print(type(mytup1))

mytup2 = ()
print(type(mytup2))