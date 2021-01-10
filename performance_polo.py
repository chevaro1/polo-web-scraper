import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           PERFORMANCE POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getPerformancePoloData(soup):
        for ultag in soup.find_all('ul', {'class': '_3Xnzg _3g8J4'}):
            for litag in ultag.find_all('li'):
                #print("\n")
                newRow = []
                for imgtag in litag.find_all("div", {"class": "_2zTHN _2AHc6 _2YocQ"}):
                    print("hello")
                    imgdiv = imgtag.find_all("div")
                    print(imgtag)
                    img = imgdiv.find("img")
                    print ("img source = " + img.get("src"))
                    #newRow.append("https://www.rjpolo.com" + imgtag["src"])
                    newRow.append(imgtag["src"])
                for productName in litag.find_all("div", {"class": "_3RqKm"}):
                    name = productName.find('h3')
                    print ("name = " + name.text + "\n")
                    newRow.append(name.text)
                    result = (gettype(productName.text))
                    newRow.append(result[0])
                    newRow.append(result[1])
                    newRow.append(result[2])
                    newRow.append(result[3])
                    newRow.append(result[4])
                    #print("product link: ")
                    #link = productName.find('a')
                    #newRow.append("https://www.rjpolo.com/" + link.get('href'))
                for productPrice in litag.find_all("div", {"class" : "_3uack"}):
                    price = productPrice.find('span', {"class": "_23ArP"})
                    print("PRICE = " + price.text)
                    price = price.text.strip()
                    newRow.append(getPrice(price))

                try:
                    pass
                    #insertdb(newRow[0], newRow[7], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[8], "RJ_Polo")
                except IndexError:
                    print("product incomplete")
                    


def PerformancePolo():
    urlList = ["https://www.performance-polo.com/tack-shop?page=2"
               ]
    print("\n" + "\n" + "Connecting to PERFORMANCE POLO WEBSITE" + "\n" + "\n")

    
    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        soup = getSoup(HTML)
        getPerformancePoloData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
 

