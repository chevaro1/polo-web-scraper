from datetime import date
import mysql.connector
from errors import addError

#local password global2020, database polo, user global
# live password VUjH2tGs7nL6xy7x, database william, user william




today = date.today()



def insertdb(img, link, name, brand, category, product, gender, colour, price, website):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="global",
            password="global2020",
            database="polo"
            )

        mycursor = mydb.cursor()
        #print("IMG = " + img + " Link= " + link + " NAME= " + name + " brand= " + brand + " category= " + category + " product= " + product + " gender= " + gender + " colour= " + colour + " price= " + str(price)  + "\n")

        date = today.strftime("%Y-%m-%d")
        #img = "www"
        #name = "boots"
        #price = "100"
        website = website.replace(' ','_')

        sql = "INSERT INTO products (date, img, link, name, brand, category, product, gender, colour, price, website) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (date, img, link, name, brand, category, product, gender, colour, price, website)

        mycursor.execute(sql,val)


        mydb.commit()

        #print(mycursor.rowcount, "record inserted.")
    except:
        print("record insertion failed")
        #print(mycursor._last_executed)
        addError(website)
