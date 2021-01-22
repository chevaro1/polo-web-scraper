from datetime import date
import mysql.connector
from errors import addError


mydb = mysql.connector.connect(
    host="localhost",
    user="william",
    password="VUjH2tGs7nL6xy7x",
    database="william"
    )

today = date.today()

mycursor = mydb.cursor()

def insertdb(img, link, name, brand, category, product, gender, colour, price, website):
    try:
        print("IMG = " + img + " Link= " + link + " NAME= " + name + " brand= " + brand + " category= " + category + " product= " + product + " gender= " + gender + " colour= " + colour + " price= " + str(price)  + "\n")

        date = today.strftime("%Y-%m-%d")
        #img = "www"
        #name = "boots"
        #price = "100"


        sql = "INSERT INTO products (date, img, link, name, brand, category, product, gender, colour, price, website) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (date, img, link, name, brand, category, product, gender, colour, price, website)

        mycursor.execute(sql,val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")
    except:
        print("record insertion failed")
        addError(website)
