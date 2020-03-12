import pymysql

# Open database connection
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="giridhar", db="testdb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.

sql = "insert into employee values('Ram','Simha',30,'M',3443)"
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
