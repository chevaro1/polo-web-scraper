from datetime import date
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="global",
    password="global2020",
    database="polo"
    )

mycursor = mydb.cursor()

def truncate():

    sql = "TRUNCATE polo.products"

    mycursor.execute(sql)

    mydb.commit()

    print("Database Truncated.")
