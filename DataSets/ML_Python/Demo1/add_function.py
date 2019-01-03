def add(num1, num2, num3= 0):
    print("Inside add func" , num1,num2, num3)



"""add(10,20)
add([10,20,30],[40,50,60],"rty")"""


#default parameter has to be last one
#No function overloading

"""def add_Multiple(*val):
    print(val)

add_Multiple(1,2,3,4,5)"""


#by default everything is public
#we can change it to private __