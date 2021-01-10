import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       SATS POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getSatsPoloData(soup):
    for ultag in soup.find_all('ul', {'class': 'products columns-4'}):
        for litag in ultag.find_all('li'):
            newRow = []
            #print("\n")
            link = litag.find('a')
            newRow.append(link.get('href'))
            for imgtag in litag.find_all("img"):
                #print (imgtag["src"])
                newRow.append(imgtag["src"])
            for productName in litag.find_all("h2", {"class": "woocommerce-loop-product__title"}):
                #print (productName.text)
                newRow.append(productName.text)
                result = (gettype(productName.text))
                newRow.append(result[0])
                newRow.append(result[1])
                newRow.append(result[2])
                newRow.append(result[3])
                newRow.append(result[4])
            for productPrice in litag.find_all("span", {"class" : "price"}):
                #print(productPrice.text)
                newRow.append(getPrice(productPrice.text))
                
            
            
            insertdb(newRow[1], newRow[0], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[7], newRow[8], "sats_polo")
                    

def SatsPolo():
    urlList = ["https://www.satsfaction.com/shop/page/1/",
         "https://www.satsfaction.com/shop/page/2/",
         "https://www.satsfaction.com/shop/page/3/",
         "https://www.satsfaction.com/shop/page/4/",
         "https://www.satsfaction.com/shop/page/5/",
         "https://www.satsfaction.com/shop/page/6/",
         "https://www.satsfaction.com/shop/page/7/",
         "https://www.satsfaction.com/shop/page/8/",
         "https://www.satsfaction.com/shop/page/9/"
         ]

    print("\n" + "\n" + "Connecting to SATS POLO WEBSITE" + "\n" + "\n")


    for i in urlList:
        HTML = getHTML(i)
        soup = getSoup(HTML)
        getSatsPoloData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + i + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


