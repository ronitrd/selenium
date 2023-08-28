
import mysql.connector

try:
    con=mysql.connector.connect(host="localhost",port=3306,user="ron",passwd="paswrd",database="mydb")
    curs=con.cursor()   #create cursor
    curs.execute("select * from student") # Execute query through cursor
    for row in curs:
        print(row[0],row[1])#,row[2],row[3],row[4],row[5])

    con.close()
except:
    print("Connection unsuccessful...")
print("Finished....")