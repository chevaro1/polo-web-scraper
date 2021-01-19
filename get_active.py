from datetime import date
import mysql.connector

def get_active():
    mydb = mysql.connector.connect(
        host="localhost",
        user="global",
        password="global2020",
        database="polo"
        )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM websites")

    result = mycursor.fetchall()
    fun_array = []

    for x in result:
        if (x[3] == "inactive"):
            fun_array.append(x[2])
        #print (x[1])

    return fun_array


#print(fun_array)
#fun_array.pop(0)


#arr = [hello()]

#runner = fun_array[0]
#run = globals()[runner]
#run()
