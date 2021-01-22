import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice
from errors import addError

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           CASABLANCA WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getCasablancaData(soup):
    print("entered get data")
    for divtag in soup.find_all("div", {"class": "category-products"}):
        for ultag in divtag.find_all('ul'):
            #print(ultag)
            for litag in ultag.find_all('li'):
                #print("\n")
                newRow = []
                for imgtag in litag.find_all("img", {"class" : "product-main-photo"}):
                    #print ("img source: " + imgtag["src"])
                    newRow.append(imgtag["src"])
                for productName in litag.find_all("h5"):
                    #print ("product name: " )
                    #print(productName.text)
                    name =productName.text.strip()
                    newRow.append(name)
                    result = (gettype(productName.text))
                    newRow.append(result[0])
                    newRow.append(result[1])
                    newRow.append(result[2])
                    newRow.append(result[3])
                    newRow.append(result[4])
                    link = productName.find('a')
                    #print('HREF: ')
                    newRow.append(link.get('href'))

                for productPrice in litag.find_all("div", {"class" : "price-box"}):
                    print("product price: ")
                    print(productPrice.text)
                    price = "n/a"
                    price = productPrice.text.strip()
                    newRow.append(getPrice(price))
                try:
                    insertdb(newRow[0], newRow[7], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[8], "casablanca")
                except IndexError:
                    print("product incomplete")
                    addError("casablanca")




def Casablanca():
    urlList = ["https://www.casablancapolo.com/unitedkingdom/saddles",
               "https://www.casablancapolo.com/unitedkingdom/helmet#",
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
