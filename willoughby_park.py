import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           WILLOUGHBY PARK POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getWPData(soup):
        nameList = []
        priceList = []
        imgList = []
        linkList = []
        

        for divtag in soup.find_all("div", {"class": "main-gallery-item col-md-3 col-sm-4 col-xs-6"}):
            name = divtag.find('h4')
            nameList.append(name.text)
            #print (name.text)
            price = divtag.find('p')
            #priceList.append(divtag.find('p'))
            price =(getPrice(price.text))
            priceList.append(price)
            #print (price)
            img= divtag.find('img')
            imgList.append(img.get('src'))
            #print(img.get('src'))
            link = name.find('a')
            link = link.get('href')
            #print("https://www.wppologear.co.uk/shop" + link[5:])
            linkList.append("https://www.wppologear.co.uk/shop" + link[2:])

        x = 0

        while x < len(nameList):
            newRow = []
            try:
                #print("price = " + getPrice(priceList[x]))
                newRow.append(imgList[x])
                newRow.append(linkList[x])
                newRow.append(nameList[x])
                result = (gettype(nameList[x]))
                newRow.append(result[0])
                newRow.append(result[1])
                newRow.append(result[2])
                newRow.append(result[3])
                newRow.append(result[4])
                newRow.append(priceList[x])
                #print(newRow)
            
                insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[7], newRow[8], "willoughby park polo")
            except IndexError:
                    print("product incomplete")
            x = x + 1
                




def WilloughbyPark():
    urlList = ["https://www.wppologear.co.uk/shop/polo/default.aspx"
                ]


    print("\n" + "\n" + "Connecting to WILLOUGHBY PARK POLO WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        try:
            HTML = getHTML(i)
            #print("hello")
            soup = getSoup(HTML)
            getWPData(soup)
        except:
            print("could not connect to webpage")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

