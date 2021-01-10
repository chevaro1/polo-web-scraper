import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           LA MARTINA WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getLaMartinaData(soup):
        nameList = []
        priceList = []
        imgList = []
        linkList = []
        
        #PRICE
        for pricetag in soup.find_all("div", {"class": "ProductItem__PriceList ProductItem__PriceList--showOnHover Heading"}):
            #print ("price in tag = " + repr(pricetag.text))
            price = pricetag.text
            priceList.append(price)
            

        
        #NAME
        for nametag in soup.find_all("h2", {"class": "ProductItem__Title Heading"}):
            #for titletag in nametag.find_all("a"):
            #print(nametag.text)
            nameList.append(nametag.text)
            #print("product link: ")
            link = nametag.find('a')
            linkList.append("https://tech.lamartina.com/" + link.get('href'))

        #IMAGE            
        for phototag in soup.find_all("div", {"class": "AspectRatio AspectRatio--square"}):
            #print(phototag)
            #for pictag in phototag.find_all("img", {"class": "ProductItem__Image"}):
            for pictag in phototag.find_all(lambda tag: tag.name == 'img' and tag.get('class') == ['ProductItem__Image']):
                imgList.append(pictag.get("src"))
                #print("\n")
             #   imgList.append("https://www.lamartina.com/" + pictag["src"])
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

                #print(newRow)
            
                insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[7], newRow[8], "La Martina")
            except IndexError:
                    print("product incomplete")
            x = x + 1
                




def LaMartina():
    urlList = ["https://tech.lamartina.com/collections/rider?page=2",
               "https://tech.lamartina.com/collections/rider?page=1",
               "https://tech.lamartina.com/collections/horse",
               "https://tech.lamartina.com/collections/accessories"
               ]


    print("\n" + "\n" + "Connecting to LA MARTINA WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getLaMartinaData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")





LaMartina()
