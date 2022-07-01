
import pymysql

conn = pymysql.connect(host="localhost", user="root", password="", port=3306)

cursor = conn.cursor()

qry = "create database employee"

cursor.execute(qry)

conn.close()
