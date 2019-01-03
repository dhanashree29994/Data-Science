#__init__() method works as constructor 
#its a private method
#__init__()
#starting __ means private and ending __ is predefined method.

#any function in the class takes first argument as self.
#self --> it will be called using object. self is like "this" IT BELONGS TO THE CLASS
#can access class level variable directly (with or without creating object)


class Employee:
    """Hi"""
    cname= "Accenture"
    def __init__(self, eid, ename):
        self.__emp_id = eid# this self means that this variable is instance variable.. which can be accessed globally
        self.__emp_name = ename
        print("Inside __init__() method", self.__emp_id, self.__emp_name)
    def info(self):
        print("Inside info() method",  self.__emp_id, self.__emp_name)


print(Employee.cname)

print(Employee.__doc__)

emp = Employee(101,"Dhanashree")

emp.info()
#private variables are accessible inside the same class only
#We can't use private variables outside the class

#print(emp.__emp_id)#gives error

