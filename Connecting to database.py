import cx_Oracle
con = cx_Oracle.connect('system/123@localhost:1521/xe')
cursor = con.cursor()
print(con.version)
# # cursor.execute("create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")
cursor.execute("insert into employee values(1002, 'Vaibhav', 5000000 )")
cursor.execute("select * from employee")
print(cursor.fetchall())
con.commit()
