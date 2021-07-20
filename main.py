#!/usr/bin/env python
import sys
import os
import time
from truncate_db import truncate
from main_scraper import scrapeMain
from delete_duplicate import deleteDup
import timeit
import datetime
from scrapejs import runscrape
from send_message import startMessage
from send_message import endMessage
from send_message import errorMessage
from config import insertHistoryDb
from config import removeTableWebsite
#if no sys argument just run the whole program, this is for the automated system to running
# option "1" sets the number of processes to be used by the program
# option "2" if present will open up the the otions menu
# in options menu have the following

sites = ["naylors",
        "equine_superstore",
        "equus",
        "hope_valley_saddlery",
        "online_for_equine",
        "redpost_equestrian",
        "robinsons_equestrian",
        "the_saddlery_shop",
        "ayr_equestrian",
        "derby_house_store",
        "equestrian_world",
        "equiport",
        #"houghton_country",      #cant seem to load all of the js  lazy loader problem scrapy-splash
        "ingatestone_saddlery",    # fixed
        "kramer",                  #need actual valid links otherwise working
        "randr_country",             # fixed
        "royal_equestrian",
        "imperial_equestrian",
        "robinsons_equestrian_uk",
        "fast_tack_direct",
        "tack_shop",
        "dragonfly_saddlery",
        "edgemere",
        "church_equestrian",
        "equiporium",
        "old_dairy_saddlery",
        "griggs_equestrian",
        "the_yard_equine",
        "the_ranch_store",
        "all_your_horse_needs",
        "throstlenest_saddlery",
        "just_equine",
        "rb_equestrian",
        "avily",
        "barnstaple_equestrian_supplies",
        "brendon_saddlery",
        "complete_equestrian",
        "cool_equestrian",
        "cork_farm_equestrian",
        "dash_equestrian",
        "denchworth_equestrian",
        "elite_saddlery",
        "equine_mania",
        "equitogs",
        "gilberts_equestrian",
        "hendry_equestrian_shop",
        "horse_and_rider",
        "just_horse_riders",
        "milton_equestrian",
        "retford_saddlery",
        "saddlesdane",
        "smeeth_saddlery",
        "speedgate",
        "the_paddock_pantry",
        "wadswick",
        "bareback_footwear",
        "brogini",
        "charlies",
        "chelford",
        "chobham_rider",
        "classic_dressage",
        "colne_saddlery",
        "animed_direct",
        "mole_online",
        "pet_drugs_online",
        "the_centre_line",
        "vivendi_apparel"
        ]

js_sites = ["millbry_hill",
           "horze",
           "oakfield_direct",
           "equine_essentials_direct",
           "equi_supermarket",
           "equine_superstore",
           "shires_equestrian",
           "discount_equestrian",
           "gs_equestrian"
           ]

def clearScreen():
    os.system('cls' if os.name=='nt' else 'clear')

def runNonJs():
    clearScreen()
    print("please choose the website you would like to run:")
    count = 0
    while count < len(sites):
        print(str(count) + " for: " + str(sites[count]))
        count += 1
    site = input("Enter option: ")
    if site.isnumeric() != True and int(site) < len(sites):
        print("no option available with this value, try again..")
        time.sleep(1)
        runNonJs()
        return
    res = []
    res.append(sites[int(site)])
    start = timeit.default_timer()
    scrapeMain(res, processes)
    stop = timeit.default_timer()
    print('Time: ' + str(datetime.timedelta(seconds=(stop - start))))



def runJs():
    clearScreen()
    print("please choose the website you would like to run:")
    count = 0
    while count < len(js_sites):
        print(str(count) + " for: " + str(js_sites[count]))
        count += 1
    site = input("Enter option: ")
    if site.isnumeric() != True and int(site) < len(js_sites):
        print("no option available with this value, try again..")
        time.sleep(1)
        runNonJs()
        return
    res = []
    res.append(js_sites[int(site)])
    start = timeit.default_timer()
    runscrape(res, processes)
    stop = timeit.default_timer()
    print('Time: ' + str(datetime.timedelta(seconds=(stop - start))))

def sitemap():
    clearScreen()
    print("This function is a work in progress try again later")

def truncateTable():
    clearScreen()
    truncate()

def runAllNonJs():
    clearScreen()
    start = timeit.default_timer()
    scrapeMain(sites, processes)
    stop = timeit.default_timer()
    print('Time: ' + str(datetime.timedelta(seconds=(stop - start))))

def runAllJs():
    clearScreen()
    start = timeit.default_timer()
    runscrape(js_sites, processes)
    stop = timeit.default_timer()
    print('Time: ' + str(datetime.timedelta(seconds=(stop - start))))

def importWebsites():
    removeTableWebsite()
    os.system('ssh -p 2244 william@web.gnil.net "mysqldump -u william -pVUjH2tGs7nL6xy7x william websites --no-tablespaces | gzip -f9" > tmp.sql.gz')
    os.system('gzip -df tmp.sql.gz')
    os.system('mysql -u global -pglobal2020 polo < tmp.sql')

def exportProductsTable():
    os.system('mysqldump -u global -pglobal2020 polo products --no-tablespaces> /home/webscraper/export/products.sql')
    os.system('ssh -p 2244 william@web.gnil.net "mysql -u william -pVUjH2tGs7nL6xy7x william" < /home/webscraper/export/products.sql')

def testEndMessage():
    start = timeit.default_timer()
    time.sleep(5)
    print("Please wait 5 seconds")
    stop = timeit.default_timer()
    endMessage(str(datetime.timedelta(seconds=(stop - start))))
    print('Expected Output: ' + str(datetime.timedelta(seconds=(stop - start))))

def runOption(no):
    print("option = " + no)
    methodDict = {'0': runNonJs, '1': runJs, '2': sitemap, '3': truncateTable, '4': runAllNonJs, '5': runAllJs, '6': importWebsites, '7': exportProductsTable, '8': testEndMessage}
    method = methodDict[no]
    method()


def menuHome():
    clearScreen()
    print("***********************************")
    print("Welcome to the menu!")
    print("***********************************")
    print("Please type the number of the option you want:")
    print("option 0: run a website in non JS mode")
    print("option 1: run a website in JS mode")
    print("option 2: parse sitemap (WIP)")
    print("option 3: truncate products table")
    print("option 4: run non js scraper")
    print("option 5: run js scraper")
    print("option 6: import latest websites")
    print("option 7: export products table to live server")
    print("option 8: test finish message")
    print("Or type 'esc' to exit")
    option = ''
    option = input("Enter option: ")
    if option == "esc":
        print("goodbye.")
        sys.exit()
    if option.isnumeric() != True:
        print("no option available with this value, taking you home..")
        time.sleep(1)
        menuHome()
        return
    if int(option) > 8 :
        print("no option available with this value, taking you home..")
        time.sleep(1)
        menuHome()
        return
    print("option " + option + " chosen")
    print("loading... (NOTHING THERE CURRENTLY)")
    runOption(option)

def fullScrape():
    try:
        start = timeit.default_timer()
        startMessage()
        print("Web scraper started")
        truncate()

        scrapeMain(sites, processes)
        runscrape(js_sites, processes)

        print("deleting duplicates")
        deleteDup()
        stop = timeit.default_timer()
        endMessage(str(datetime.timedelta(seconds=(stop - start))))
        print('Time: ' + str(datetime.timedelta(seconds=(stop - start))))
        time.sleep(5)
        insertHistoryDb()
        exportProductsTable()
        os.system('sudo shutdown -h 5')
    except:
        print("Full scrape failed")
        errorMessage()
        os.system('sudo shutdown -h 5')

if len(sys.argv) < 2:
    print("At least 1 argument required: ")
    print("arg 1 = number of processes to be run on")
    print("arg 2 (optional) = settings menu launcher")
    print("Quitting launcher...")
    sys.exit()

processes = int(sys.argv[1])

if len(sys.argv) > 2:
    menuHome()
else:
    fullScrape()


















#
