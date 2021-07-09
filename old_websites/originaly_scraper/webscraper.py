import mysql.connector
import time
import requests
from bs4 import BeautifulSoup
import csv
from datetime import date


today = date.today()

bag = ["boot bag", "hat bag", "helmet bag", "mallet bag", "saddle bag", "kit bag", "bridle bag", "stick bag",
       "tack bag"]
poloboot = ["zip", "riding boot", "polo boot"]
boot = ["tendon boot", "over reach", "tendon", "sport boot", "skid boot", "sports boot"]
kneepads = ["kneepad", "knee pad", "kneeguard"]
ball = ["ball"]
girth = ["overgirth", "girth"]
glove = ["glove", "ona"]
bridle = ["brow band", "nose band", "martingale", "rein", "noseband", "bridle", "breastplate"]
bit = ["gag", "pelham", "bit", "bomber", "happy tongue"]
clothes = ["t-shirt", "bracelet", "gilet", "belt", "alpargata", "cap"]
whip = ["whip"]
helmet = ["helmet"]
saddle = ["saddle"]
glasses = ["glasses", "goggles", "lens"]
chaps = ["chap"]
headcollar = ["headcollar", "leadrope", "lead rope"]
mallet = ["mallet", "stick", "cane"]
trousers = ["jodphurs", "breeches", "whites"]
socks = ["socks"]
bandages = ["bandage"]
spurs = ["spur"]

product = [bag, poloboot, kneepads, ball, girth, glove, bridle,
                  bit, clothes, whip, helmet, saddle, boot, glasses, chaps,
           headcollar, mallet, trousers, socks, bandages, spurs]

categories = ["bag", "poloboot", "kneepads", "ball", "girth", "glove", "bridle",
                  "bit", "clothes", "whip", "helmet", "saddle", "boot", "glasses",
              "chaps", "headcollar", "mallet", "trousers", "socks", "bandages", "spurs"]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       GET HTML
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getHTML(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    print("request complete")
    return response.content

def getSoup(html):
    soup = BeautifulSoup(html, "html.parser")
    #print (soup.prettify())
    return soup


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      get product name and category
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def gettype(prodname):
    prodname = prodname.lower()

    count = 0
    
    while count < len(product):
        count1 = 0
        current = product[count]
        while count1 < len(current):
            if product[count][count1] in prodname:
                return categories[count], product[count][count1]
            count1 += 1
        count += 1

    return "unknown", "unkown"


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       uplaod to database
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


mydb = mysql.connector.connect(
    host="localhost",
    user="william",
    password="global2020",
    database="polo"
    )


mycursor = mydb.cursor()

def insertdb(img, name, product, category, price, website):
    print("IMG = " + img + " NAME= " + name + " product= " + product + " category= " + category + " price= " + price  + "\n")

    date = today.strftime("%Y-%m-%d")
    #img = "www"
    #name = "boots"
    #price = "100"
    
    
    sql = "INSERT INTO products (date, img, name, product, category, price, website) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (date, img, name, product, category, price, website)

    mycursor.execute(sql,val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")


list_of_rows =[]

def addRow(newRow):

    insertdb(newRow[0],newRow[1],newRow[2])


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       SATS POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getSatsPoloData(soup):
    for ultag in soup.find_all('ul', {'class': 'products columns-4'}):
        for litag in ultag.find_all('li'):
            newRow = []
            #print("\n")
            for imgtag in litag.find_all("img"):
                #print (imgtag["src"])
                newRow.append(imgtag["src"])
            for productName in litag.find_all("h2", {"class": "woocommerce-loop-product__title"}):
                #print (productName.text)
                newRow.append(productName.text)
                product, category = (gettype(productName.text))
                newRow.append(product)
                newRow.append(category)
            for productPrice in litag.find_all("span", {"class" : "price"}):
                #print(productPrice.text)
                newRow.append(productPrice.text)
            
            
            insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], "sats_polo")
                    

def SatsPolo():
    urlList = ["https://www.satsfaction.com/shop/page/1/",
         "https://www.satsfaction.com/shop/page/2/",
         "https://www.satsfaction.com/shop/page/3/",
         "https://www.satsfaction.com/shop/page/4/",
         "https://www.satsfaction.com/shop/page/5/",
         "https://www.satsfaction.com/shop/page/6/",
         "https://www.satsfaction.com/shop/page/7/",
         "https://www.satsfaction.com/shop/page/8/",
         "https://www.satsfaction.com/shop/page/9/"]

    print("\n" + "\n" + "Connecting to SATS POLO WEBSITE" + "\n" + "\n")


    for i in urlList:
        HTML = getHTML(i)
        soup = getSoup(HTML)
        getSatsPoloData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + i + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           RJPOLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getRJPoloData(soup):
        for ultag in soup.find_all('ul', {'class': 'product-list list-reset'}):
            for litag in ultag.find_all('li'):
                #print("\n")
                newRow = []
                for imgtag in litag.find_all("img"):
                    #print ("https://www.rjpolo.com/" + imgtag["src"])
                    newRow.append("https://www.rjpolo.com" + imgtag["src"])
                for productName in litag.find_all("h2", {"class": "product-item-title ib-m"}):
                    #print (productName.text)
                    name = productName.text
                    newRow.append(name)
                    product, category = (gettype(productName.text))
                    newRow.append(product)
                    newRow.append(category)
                for productPrice in litag.find_all("div", {"class" : "product-price ib-m"}):
                    #print(productPrice.text)
                    price = productPrice.text
                    newRow.append(price)
                insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], "RJ_Polo")

def RJPolo():
    urlList = ["https://www.rjpolo.com/instinct-polo-helmets-70-c.asp",
               "https://www.rjpolo.com/polo-helmet--faceguards-21-c.asp",
               "https://www.rjpolo.com/oakley-glasses-69-c.asp",
               "https://www.rjpolo.com/polo-goggles-27-c.asp",
               "https://www.rjpolo.com/polo-boots--spurs-22-c.asp",
               "https://www.rjpolo.com/rj-polo-bags-30-c.asp",
               "https://www.rjpolo.com/polo-clothing-and-polo-white-jeans-26-c.asp",
               "https://www.rjpolo.com/polo-kneepads-64-c.asp",
               "https://www.rjpolo.com/polo-elbow-pads-23-c.asp",
               "https://www.rjpolo.com/polo-gloves--wrist-supports-24-c.asp",
               "https://www.rjpolo.com/polo-mallets--balls-28-c.asp",
               "https://www.rjpolo.com/polo-whips-25-c.asp",
               "https://www.rjpolo.com/argentine-polo-belts-49-c.asp",
               "https://www.rjpolo.com/rj-polo-bundles-50-c.asp",
               "https://www.rjpolo.com/bomber-bits-62-c.asp",
               "https://www.rjpolo.com/polo-saddles--fittings-40-c.asp",
               "https://www.rjpolo.com/polo-bridles-32-c.asp",
               "https://www.rjpolo.com/polo-bits-33-c.asp",
               "https://www.rjpolo.com/polo-boots-bandages-headcollars-kit--tack-bags-34-c.asp",
               "https://www.rjpolo.com/cirencester-park-polo-club-clothing-82-c.asp",
               "https://www.rjpolo.com/argentine-dog-collars-and-leads-80-c.asp",
               "https://www.rjpolo.com/polo-belts-79-c.asp",
               "https://www.rjpolo.com/polo-stable--vet-supplies-17-c.asp",
               "https://www.rjpolo.com/a-selection-of--polo-sheets-and-polo-rugs-for-your-horse-37-c.asp",
               "https://www.rjpolo.com/various-polo-equipment---a-selection-of-polo-items-for-your-horse-from-studs-to-pads-38-c.asp"
               ]
    print("\n" + "\n" + "Connecting to RJ POLO WEBSITE" + "\n" + "\n")

    
    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        soup = getSoup(HTML)
        getRJPoloData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       TALLY HO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

list_of_rows =[]

def addRow(newRow):

    list_of_rows.append(newRow)

def getTallyHoData(soup):
        nameList = []
        priceList = []
        imgList = []
        

        for divtag in soup.find_all("div", {"class": "priceoptions"}):
            #print (divtag.text)
            #price = formatText(divtag.text)
            price = divtag.text
            priceList.append(price)

        for nametag in soup.find_all("div", {"class": "name"}):
            for titletag in nametag.find_all("a"):
                    #print(titletag.text)
                    nameList.append(titletag.text)
        for phototag in soup.find_all("div", {"class": "thumb"}):
            for pictag in phototag.find_all("img"):
                #print (pictag["src"])
                #print("\n")
                imgList.append("https://www.tallyhofarm.co.uk" + pictag["src"])
                break

        x = 0

        while x < len(nameList):
            newRow = []
            
            newRow.append(imgList[x])
            newRow.append(nameList[x])
            product, category = (gettype(nameList[x]))
            newRow.append(product)
            newRow.append(category)
            newRow.append(priceList[x])
            
            addRow(newRow)
            x = x + 1
                
        #print("outputs: ", list_of_rows)


def upload():
    count = 0
    while count < len(list_of_rows):
        insertdb(list_of_rows[count][0],list_of_rows[count][1],list_of_rows[count][2],
                 list_of_rows[count][3],list_of_rows[count][4], "tally_ho")
        count += 1




def TallyHo():
    urlList = ["https://www.tallyhofarm.co.uk/polo-equipment/c29?page=5",
               "https://www.tallyhofarm.co.uk/polo-equipment/c29?page=4",
               "https://www.tallyhofarm.co.uk/polo-equipment/c29?page=3",
               "https://www.tallyhofarm.co.uk/polo-equipment/c29?page=2",
               "https://www.tallyhofarm.co.uk/polo-equipment/c29?page=1"]


    print("\n" + "\n" + "Connecting to TALLY HO WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getTallyHoData(soup)
        upload()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           CASABLANCA WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getCasablancaData(soup):
    print("entered get data")
    for divtag in soup.find_all("div", {"class": "category-products"}):
        for ultag in divtag.find_all('ul'):
            #print(ultag)
            for litag in ultag.find_all('li'):
                print("\n")
                newRow = []
                for imgtag in litag.find_all("img", {"class" : "product-main-photo"}):
                    #print ("img source: " + imgtag["src"])
                    newRow.append(imgtag["src"])
                for productName in litag.find_all("h5"):
                    #print ("product name: " + productName.text)
                    name =productName.text.strip()
                    newRow.append(name)
                    product, category = (gettype(productName.text))
                    newRow.append(product)
                    newRow.append(category)
                for productPrice in litag.find_all("div", {"class" : "price-box"}):
                    #print("product price: " + productPrice.text)
                    price = "n/a"
                    price = productPrice.text.strip()
                    newRow.append(price)
                insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], "casablanca")



def Casablanca():
    urlList = ["https://www.casablancapolo.com/unitedkingdom/saddles",
               #"https://www.casablancapolo.com/unitedkingdom/helmet#",
               "https://www.casablancapolo.com/unitedkingdom/boots",
               "https://www.casablancapolo.com/unitedkingdom/kneeguards",
               "https://www.casablancapolo.com/unitedkingdom/gloves",
               "https://www.casablancapolo.com/unitedkingdom/polo-elbow-pads",
               "https://www.casablancapolo.com/unitedkingdom/base-layers",
               "https://www.casablancapolo.com/unitedkingdom/accessory",
               "https://www.casablancapolo.com/unitedkingdom/whips",
               "https://www.casablancapolo.com/unitedkingdom/saddle-fittings",
               "https://www.casablancapolo.com/unitedkingdom/bridles",
               "https://www.casablancapolo.com/unitedkingdom/polo-balls",
               "https://www.casablancapolo.com/unitedkingdom/bags",
               "https://www.casablancapolo.com/unitedkingdom/t-shirts",
               "https://www.casablancapolo.com/unitedkingdom/polos",
               "https://www.casablancapolo.com/unitedkingdom/shirts",
               "https://www.casablancapolo.com/unitedkingdom/knits",
               "https://www.casablancapolo.com/unitedkingdom/jackets-outerwear",
               "https://www.casablancapolo.com/unitedkingdom/trousers",
               "https://www.casablancapolo.com/unitedkingdom/leather-goods",
               "https://www.casablancapolo.com/unitedkingdom/accessories",
               "https://www.casablancapolo.com/unitedkingdom/women"
               ]


    print("\n" + "\n" + "Connecting to CASABLANCA WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getCasablancaData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           POLOSPLICE WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getPoloSpliceData(soup):
    for ultag in soup.find_all('ul', {'class': 'productGrid'}):
        for litag in ultag.find_all('li'):
            newRow = []
            #print("\n")
            for imgtag in litag.find_all("img"):
                #print (imgtag["src"])
                newRow.append(imgtag["src"])
            for productName in litag.find_all("h4", {"class": "card-title"}):
                #print (productName.text)
                name = productName.text
                newRow.append(name)
                product, category = (gettype(productName.text))
                newRow.append(product)
                newRow.append(category)
                print('\n' + 'name = ' + name)
            for productPrice in litag.find_all("span", {"class" : "price price--withTax"}):
                #print(productPrice.text)
                price = productPrice.text
                if not price:
                    price = "n/a"
                print('\n' + 'price = ' + price)
                newRow.append(price)

            insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], "polo splice")



    




def poloSplice():
    urlList = ["https://polosplice.co.uk/ona-polo/",
               "https://polosplice.co.uk/gift-items/",
               "https://polosplice.co.uk/hook-polo/",
               "https://polosplice.co.uk/instinct-polo-helmet-new-design/",
               "https://polosplice.co.uk/armis-polo-helmets/",
               "https://polosplice.co.uk/salvavita-polo-helmet/",
               "https://polosplice.co.uk/instinct-polo-helmet/",
               "https://polosplice.co.uk/horse-rugs/",
               "https://polosplice.co.uk/stable-yard-accessories/",
               "https://polosplice.co.uk/polo-mallets/",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=1",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=2",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=3",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=4",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=5",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=6",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=1",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=2",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=3",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=4",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=5",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=6",
               "https://polosplice.co.uk/tack?sort=newest&page=1",
               "https://polosplice.co.uk/tack?sort=newest&page=2",
               "https://polosplice.co.uk/tack?sort=newest&page=3",
               "https://polosplice.co.uk/tack?sort=newest&page=4",
               "https://polosplice.co.uk/tack?sort=newest&page=5",
               "https://polosplice.co.uk/tack?sort=newest&page=6",
               "https://polosplice.co.uk/tack?sort=newest&page=7"
               ]


    print("\n" + "\n" + "Connecting to POLO SPLICE WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getPoloSpliceData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           PORTO POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getPortoPoloData(soup):
        nameList = []
        priceList = []
        imgList = []
        

        for divtag in soup.find_all("div", {"class": "prodprice"}):
            #print (divtag.text)
            price = divtag.text
            priceList.append(price)

        for nametag in soup.find_all("div", {"class": "prodname"}):
            for titletag in nametag.find_all("a"):
                    #print(titletag.text)
                    nameList.append(titletag.text)
        for phototag in soup.find_all("div", {"class": "prodimage allprodimages"}):
            for pictag in phototag.find_all("img"):
                #print (pictag["src"])
                #print("\n")
                imgList.append("https://portopolo.com/" + pictag["src"])
                break

        x = 0

        while x < len(nameList):
            newRow = []
            
            newRow.append(imgList[x])
            newRow.append(nameList[x])
            product, category = (gettype(nameList[x]))
            newRow.append(product)
            newRow.append(category)
            newRow.append(priceList[x])
            
            addRow(newRow)
            x = x + 1
                




def PortoPolo():
    urlList = ["https://portopolo.com/search.php?nobox=&scat=&pg=1",
               "https://portopolo.com/search.php?nobox=&scat=&pg=2",
               "https://portopolo.com/search.php?nobox=&scat=&pg=3",
               "https://portopolo.com/search.php?nobox=&scat=&pg=4",
               "https://portopolo.com/search.php?nobox=&scat=&pg=5",
               "https://portopolo.com/search.php?nobox=&scat=&pg=6",
               "https://portopolo.com/search.php?nobox=&scat=&pg=7",
               "https://portopolo.com/search.php?nobox=&scat=&pg=8",
               "https://portopolo.com/search.php?nobox=&scat=&pg=9",
               "https://portopolo.com/search.php?nobox=&scat=&pg=10",
               "https://portopolo.com/search.php?nobox=&scat=&pg=11",
               "https://portopolo.com/search.php?nobox=&scat=&pg=12",
               "https://portopolo.com/search.php?nobox=&scat=&pg=13",
               "https://portopolo.com/search.php?nobox=&scat=&pg=14",
               "https://portopolo.com/search.php?nobox=&scat=&pg=15"]


    print("\n" + "\n" + "Connecting to PORTO POLO WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getPortoPoloData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




#SatsPolo()
#RJPolo()
#TallyHo()
#Casablanca()
#poloSplice()
PortoPolo()

print("\n" + "\n" + "Download Complete")



