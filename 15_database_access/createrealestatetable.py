

import pymysql
# Open database connection
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="giridhar", db="testdb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Drop table if it already exist using execute() method.
cursor.execute("DROP TABLE IF EXISTS realestate")

# Create table as per requirement
sql = """CREATE TABLE realestate(
         street  CHAR(200),
         city char(100),
         zipcode  CHAR(20),
         state char(100),  
         beds char(30))"""

cursor.execute(sql)

print("table created successfully")

# disconnect from server
db.close()



