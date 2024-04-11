import datetime
import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(user='root', password='root',database = 'emp')
cursor = cnx.cursor()

# Run a query
query = ("SELECT first_name, last_name, hire_date FROM employees WHERE hire_date BETWEEN %s AND %s")

hire_start = datetime.date(2007, 1, 1)
hire_end = datetime.date(2007, 12, 31)

cursor.execute(query, (hire_start, hire_end))

for (first_name, last_name, hire_date) in cursor:
    print("{}, {} was hired on {:%d %b %Y}".format(
        last_name, first_name, hire_date))
    
# Close the connection
cursor.close()
cnx.close()