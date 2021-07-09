import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice
from errors import addError

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           KRONO POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getkronoData(soup):
        nameList = []
        priceList = []
        imgList = []
        linkList = []
        #print(soup.prettify)

        for divtag in soup.find_all("div", {"class": "product-layout product-list col-xs-12"}):
            #print("hello there")
            name = divtag.find('div', {"class": "caption"})
            name1 = name.find('h4')
            link = name1.find('a')
            link = link.get('href')
            nameList.append(name1.text)
            #print ("name = " + name1.text)
            price = divtag.find('div', {"class": "price"})
            #priceList.append(divtag.find('p'))
            price =(getPrice(price.text))
            priceList.append(price)
            #print (price)
            img= divtag.find('img')
            imgList.append(img.get('src'))
            #print(img.get('src'))
            #link = name.find('a')
            #link = name.get('href')
            #print(link)
            linkList.append(link)

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

                insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[7], newRow[8], "krono polo")
            except IndexError:
                    print("product incomplete")
                    addError("krono polo")
            x = x + 1





def KronoPolo():
    urlList = ["https://www.kronopolo.com/accessories",
               "https://www.kronopolo.com/bags",
               "https://www.kronopolo.com/beanies",
               "https://www.kronopolo.com/polo-belt",
               "https://www.kronopolo.com/polo-boots",
               "https://www.kronopolo.com/caps",
               "https://www.kronopolo.com/elbow-guards",
               "https://www.kronopolo.com/gloves",
               "https://www.kronopolo.com/polo-helmet",
               "https://www.kronopolo.com/hoodies",
               "https://www.kronopolo.com/knee-pads",
               "https://www.kronopolo.com/mask",
               "https://www.kronopolo.com/polo-trousers",
               "https://www.kronopolo.com/saddles",
               "https://www.kronopolo.com/shirts",
               "https://www.kronopolo.com/polo-socks",
               "https://www.kronopolo.com/sunglasses",
               "https://www.kronopolo.com/polo-team-equipment",
               "https://www.kronopolo.com/team-shirts",
               "https://www.kronopolo.com/teamwear",
               "https://www.kronopolo.com/tees",
               "https://www.kronopolo.com/underwear",
               "https://www.kronopolo.com/polo-whips"
                ]


    print("\n" + "\n" + "Connecting to KRONO POLO WEBSITE" + "\n" + "\n")


    x = 0

    for i in urlList:
        x += 1
        try:
            HTML = getHTML(i)
            #print("hello")
            soup = getSoup(HTML)
            getkronoData(soup)
        except:
            print("could not connect to webpage")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
