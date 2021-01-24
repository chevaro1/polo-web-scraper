import datetime
import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="global",
    password="global2020",
    database="polo"
    )

today = datetime.datetime.now()

mycursor = mydb.cursor()

log = []


def addError(site):

    #print("error found with " + site)
    length = len(log)

    if len(log) > 0:
        if any(site in sub1 for sub1 in log):
            #print(site + " present")
            for i in range(length):
                #print("iterating through log")
                if site in log[i][0]:
                    #print("site found")
                    log[i][1] += 1

        else:
            #print("not present")
            log.append([site,1])
    else:
        #print("log empty, adding to log")
        log.append([site,1])

    #print(log)


def saveErrorLog():
    length = len(log)
    for i in range(length):
        saveLogData(log[i][0], log[i][1])


def saveLogData(site, errors):

    sql = "INSERT INTO error_log (datetime, website, errors) VALUES (%s, %s, %s)"
    val = (today, site, errors)

    mycursor.execute(sql,val)

    mydb.commit()
