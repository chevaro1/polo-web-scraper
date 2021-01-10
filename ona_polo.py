import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           ROXTONS WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getOnaData(soup):
    for ultag in soup.find_all('ul', {'class': 'products columns-4'}):
        for litag in ultag.find_all('li'):
            newRow = []
            #print(litag)
            for imgtag in litag.find_all("img"):
                #print ("image link = " + imgtag["src"])
                newRow.append(imgtag["src"])
                break 
            #for productName in litag.find_all("a", {"class": "ProductDetails"}):
            #for productName in litag.find_all({"class": "ProductDetails"}):
            for productLink in litag.find_all("a", {"class": "woocommerce-LoopProduct-link woocommerce-loop-product__link"}):
                #link = productLink.find('a', {"class": "woocommerce-LoopProduct-link woocommerce-loop-product__link"})
                #print("product link = " + productLink.get('href'))
                newRow.append(productLink.get('href'))
            for productName in litag.find_all("div", {"class": "inner_product_header_cell"}):
                #print("HELLO THERE " + "\n")
                #print ("product name = " + productName.find('h2').text)
                #for prof in productName.find_all`
                link = productName.find('h2')
                name = link.text
                newRow.append(name)
                result = (gettype(name))
                newRow.append("ona")
                newRow.append(result[1])
                newRow.append(result[2])
                newRow.append(result[3])
                newRow.append(result[4])
                #print("https://www.roxtons.co.uk/" + link.get('href'))
                #newRow.append("https://www.roxtons.co.uk/" + link.get('href'))
                #print('\n' + 'name = ' + name)
            for productPrice in litag.find_all("div", {"class" : "inner_product_header_cell"}):
                #print("price = " + productPrice.text)
                price = productPrice.find('bdi').text
                if not price:
                    price = "n/a"
                #print('\n' + 'price in here = ' + price)
                newRow.append(getPrice(price))
                break

            print(newRow)
            try:
                insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[7], newRow[8], "ona polo")
            except IndexError:
                    print("product incomplete")














def onaPolo():
    urlList = ["https://www.onapolo.com/product-category/ona-polo-gloves/",
               "https://www.onapolo.com/product-category/elbow-pads/",
               "https://www.onapolo.com/product-category/polo-jeans/",
               "https://www.onapolo.com/product-category/base-layers/",
               "https://www.onapolo.com/product-category/whips/",
               "https://www.onapolo.com/product-category/boot-bag/",
               "https://www.onapolo.com/product-category/boots/",
               "https://www.onapolo.com/product-category/saddles/"
               ]


    print("\n" + "\n" + "Connecting to ONA POLO WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getOnaData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

