from datetime import date
import mysql.connector

def get_active():
    mydb = mysql.connector.connect(
        host="localhost",
        user="william",
        password="VUjH2tGs7nL6xy7x",
        database="william"
        )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM websites")

    result = mycursor.fetchall()
    fun_array = []
    #print("in get active")

    for x in result:
        print("looping through websites")
        if (x[3] == "active"):
            fun_array.append(x[2])
        #print (x[1])

    return fun_array


#print(fun_array)
#fun_array.pop(0)


#arr = [hello()]

#runner = fun_array[0]
#run = globals()[runner]
#run()
