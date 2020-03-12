import pymysql
# Open database connection
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="giridhar", db="tcl")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.
sql = "select * from citi_info"

try:
   # Execute the SQL command  
   cursor.execute(sql)
   # Fetch all the rows in a list of lists.
   results = cursor.fetchall()
   for row in results:
      print(row)
 
   
      # Now print fetched result
      #print(city,ctype,state)
except:
   print ("Error: unable to fecth data")

# disconnect from server
db.close()
