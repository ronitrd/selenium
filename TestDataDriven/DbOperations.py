# insert, update, delete

insert_query="insert into student values(104,'Kim')"
update_query="update student set sName='Mary' where sid=104"
delete_query="delete from student where sid=104"

import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",port=3306,user="ron",passwd="paswrd",database="mydb")
    curs=con.cursor()   #create cursor
    curs.execute(insert_query) # Execute query through cursor
    con.commit()    #commit transaction
    con.close()
except:
    print("Connection unsuccessful...")
print("Finished....")