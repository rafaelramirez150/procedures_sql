import datetime
import mysql.connector

cnx=mysql.connector.connect(user='root', password='root', database='emp')
cursor=cnx.cursor()

hire_start=datetime.date(2007,1,1)
hire_end=datetime.date(2007,12,31)

#cursor.execute(query,(hire_start, hire_end))
cursor.callproc("ns",[hire_start, hire_end])

for results in cursor.stored_results():
    details=results.fetchall()

for det in details:
    print(det)

cursor.close()
cnx.close()