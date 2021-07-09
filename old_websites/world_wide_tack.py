import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice
from errors import addError


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           WORLD WIDE TACK WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getWorldWideTackData(soup):
        nameList = []
        priceList = []
        imgList = []
        linkList = []

        #PRICE
        for pricetag in soup.find_all("span", {"class": "woocommerce-Price-amount amount"}):
            #print ("price: " + pricetag.text)
            price = pricetag.text
            priceList.append(price)


        #NAME
        for nametag in soup.find_all("div", {"class": "whiteBox"}):
            #print("product link: ")
            link = nametag.find('a')
            linkList.append(link.get('href'))
            for titletag in nametag.find_all("h2"):
                #print("name: " + titletag.text)
                name = titletag.text
                #name.strip('"')
                nameList.append(name)


        #IMAGE
        for phototag in soup.find_all("a", {"class": "imageContainer"}):
            for pictag in phototag.find_all("img"):
                #print ("img scr: " + pictag["src"])
                #print("\n")
                imgList.append(pictag["src"])
                break

        x = 0

        while x < len(nameList):
            newRow = []
            try:
                newRow.append(imgList[x])
                newRow.append(linkList[x])
                newRow.append(nameList[x])
                result = (gettype(nameList[x]))
                newRow.append(result[0])
                newRow.append(result[1])
                newRow.append(result[2])
                newRow.append(result[3])
                newRow.append(result[4])
                newRow.append(getPrice(priceList[x]))


                insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[7], newRow[8], "World Wide Tack")
            except IndexError:
                    print("product incomplete")
                    addError("world wide tack")
            x = x + 1





def WorldWideTack():
    urlList = ["https://www.worldwidetack.com/category/polo-equipment/polo-accessories/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-bits/4-rings/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-bits/3-rings/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-bits/big-ring-gags/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-bits/pelhams/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-leatherwork/"
               ]


    print("\n" + "\n" + "Connecting to WORLD WIDE TACK WEBSITE" + "\n" + "\n")


    x = 0

    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getWorldWideTackData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
