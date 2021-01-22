import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice
from errors import addError

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           ROXTONS WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getRoxtonsData(soup):
    for ultag in soup.find_all('ul', {'class': 'productgrid--items'}):
        for litag in ultag.find_all('li'):
            newRow = []
            #print(litag)
            for imgtag in litag.find_all("img"):
                print ("image link = " + imgtag["src"])
                newRow.append(imgtag["src"])
                break
            #for productName in litag.find_all("a", {"class": "ProductDetails"}):
            #for productName in litag.find_all({"class": "ProductDetails"}):
            for productName in litag.find_all("div", {"class": "productitem--info"}):
                #print("HELLO THERE " + "\n")
                print ("product name = " + productName.find('a').text)
                #for prof in productName.find_all`
                link = productName.find('a')
                name = link.text
                newRow.append(name)
                result = (gettype(name))
                newRow.append(result[0])
                newRow.append(result[1])
                newRow.append(result[2])
                newRow.append(result[3])
                newRow.append(result[4])
                print("https://www.roxtons.co.uk/" + link.get('href'))
                newRow.append("https://www.roxtons.co.uk/" + link.get('href'))
                #print('\n' + 'name = ' + name)
            for productPrice in litag.find_all("div", {"class" : "price--main"}):
                #print("price = " + productPrice.text)
                price = productPrice.find('span', {"class" : "money"}).text
                if not price:
                    price = "n/a"
                print('\n' + 'price in here = ' + price)
                newRow.append(getPrice(price))
                break

            try:
                insertdb(newRow[0], newRow[7], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[8], "Roxtons")
            except IndexError:
                    print("product incomplete")
                    addError("roxtons")



def roxtons():
    urlList = ["https://www.roxtons.co.uk/collections/polo?view=view-48"
               ]


    print("\n" + "\n" + "Connecting to ROXTONS WEBSITE" + "\n" + "\n")


    x = 0

    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getRoxtonsData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
