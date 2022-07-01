
import pymysql
from prettytable import from_db_cursor

conn = pymysql.connect(host="localhost", user="root", password="", port=3306, database="employee")

cursor = conn.cursor()

qry = "select * from emp"

cursor.execute(qry)

# for rec in cursor.fetchall():
#     print(rec)

pt = from_db_cursor(cursor)
pt.align['empname'] = "l"
pt.align['salary'] = "r"

conn.close()

print(pt)