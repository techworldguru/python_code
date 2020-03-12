import pymysql

# Open database connection
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="giridhar", db="testdb" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

fobj = open("realestate.csv","r")

for line in fobj :
    line = line.strip()
    data = line.split(",")

    street,city,zipcode,state,beds =  data[0],data[1],data[2],data[3],data[4]
    print(street,city,zipcode,state,beds)
    sql = "insert into realestate(street,city,zipcode,state,beds) values('{}','{}','{}','{}','{}')".format(street,city,zipcode,state,beds)
    cursor.execute(sql)
    #print(sql)
# disconnect from server
db.commit()
db.close()
fobj.close()
