from datetime import date
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="global",
    password="global2020",
    database="polo"
    )

mycursor = mydb.cursor()

def deleteDup():

    #sql = "DELETE FROM products WHERE id NOT IN (SELECT MIN(id) as id FROM products GROUP BY date,img,name,brand,category,product,gender,colour,price,website)"
    sql = "DELETE FROM products WHERE id NOT IN (SELECT MIN(id) as id FROM (SELECT * FROM products) AS products GROUP BY date,img,name,brand,category,product,gender,colour,price,website)"

    mycursor.execute(sql)

    mydb.commit()

    print("Duplicates Deleted.")
