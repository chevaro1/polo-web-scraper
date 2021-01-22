from datetime import date
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="william",
    password="VUjH2tGs7nL6xy7x",
    database="william"
    )

mycursor = mydb.cursor()

def truncate():

    sql = "TRUNCATE polo.products"

    mycursor.execute(sql)

    mydb.commit()

    print("Database Truncated.")
