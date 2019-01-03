class Person:
    def __init__(self, eid, ename):
        self.__emp_id = eid
        self.__emp_name = ename
        print("Inside __init__() method of Person", self.__emp_id, self.__emp_name)
    def pinfo(self):
        print("Pinfo is in Person class")

class Human:
    def __init__(self, eid, ename):
        self.__emp_id = eid
        self.__emp_name = ename
        print("Inside __init__() method of Human", self.__emp_id, self.__emp_name)
    def hinfo(self):
        print("hinfo is in Human class")

class Employee(Person, Human):
    """Hi"""
    cname= "Accenture"
    def __init__(self, eid, ename):
        super().__init__(102, "Chinmay")
        self.__emp_id = eid
        self.__emp_name = ename
        print("Inside __init__() method", self.__emp_id, self.__emp_name)
    def info(self):
        print("Inside info() method",  self.__emp_id, self.__emp_name)


obj = Employee(101, "Dhanu")
obj.pinfo()
obj.hinfo()

# No diamond problem 
#It checks the method in all the classes sequentially.Calls the method of first available.
#if we want method of second class then We will create object of that
# particular class and tehn call teh method







"""OVERRIDING"""

"""first class method will be called in this case as well."""




