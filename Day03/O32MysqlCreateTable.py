
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", port=3306, database="employee")

cursor = conn.cursor()

qry = """create table emp (
empid varchar(7) PRIMARY KEY,
empname varchar(50) NOT NULL,
salary int NOT NULL
)
"""
cursor.execute(qry)
