
import pymysql

# Open database connection
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="giridhar", db="tcl" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

with open("realestate.csv") as fobj:
    for line in fobj:
        line = line.strip()
        output = line.split(",")
        sql = "insert into citi_info values('{}','{}','{}');".format(output[1],output[7],output[3])
        #print(sql)

        # Prepare SQL query to INSERT a record into the database.
    
        try:
            cursor.execute(sql)
            # Commit your changes in the database
            db.commit()
        except Exception as error:
            # Rollback in case there is any error
            db.rollback()
            print(error)
            

# disconnect from server
db.close()
