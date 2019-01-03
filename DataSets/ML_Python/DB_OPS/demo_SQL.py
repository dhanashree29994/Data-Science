import sqlite3

con = sqlite3.connect("C:\\Users\\pdc3a-training.pdc3a\\Desktop\\info.db")

#IP address| port| db name |username and password


cr = con.cursor()

"""cr.execute("Select * from emp")
res = cr.fetchall()
print(res)

#print(cr.fetchmany(3)) 
#print(cr.fetchone())


for val in res:
    #print(val)
    print(val[0],"  ",val[1])



cr.execute("delete from emp where  eid = ?",(int(input("ENTER ID ")), ))
con.commit()


cr.execute("select * from emp ")
print(cr.fetchall())

"""


"""Lambda function"""


sum = lambda num1,num2:num1+num2

print(sum(10,50))



