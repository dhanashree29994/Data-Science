
def add_dec(anyfunc):
    def inner(*val):
        print("in inner", val)
        anyfunc(*val)
        print("In add decorator" , anyfunc.__name__)
    return inner

@add_dec
def add():
    print("Add function")
@add_dec
def login(uname, password):
    print("Inside login", uname, password)


add()
login("Admin", "admin")
