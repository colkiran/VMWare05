

import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", port=3306, database="employee")

cursor = conn.cursor()

qry = "insert into emp values ('EMP003', 'Pete Sampras', 65000)"

cursor.execute(qry)

conn.close()