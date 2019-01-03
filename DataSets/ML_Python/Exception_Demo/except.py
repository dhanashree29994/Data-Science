#Exception is super class
# valueError different types
#/ by 0
# Type Error giving wrong parameter to a function
#IO Error
#Index Error 
# All Are runtime exceptions
#Since the code is interpreted not compiled.

#Without exception in except
try:
    ans = 10/0
    print(ans)
except ZeroDivisionError as e :# blank except means any exception should be handled
    print("Except an excep", e)
finally:
    print("in finally")

print("After except")

#With exception in except
"""try:
    ans = 10/0
    print(ans)
except ZeroDivisionError:# blank except means any exception should be handled
    print("Except an excep")


print("After except")"""





