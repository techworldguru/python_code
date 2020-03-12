#!/usr/bin/python

import pymysql

# Open database connection
db = pymysql.connect(host="localhost", port=3306, user="root", passwd="giridhar", db="testdb" )

cur = db.cursor()
cur.execute("SELECT NOW()")
print(cur.fetchall())
cur.close()
cur.close()
