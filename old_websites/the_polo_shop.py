import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice
from errors import addError

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           THE POLO SHOP WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getThePoloShopData(soup):
    for ultag in soup.find_all('ul', {'class': 'ProductList'}):
        for litag in ultag.find_all('li'):
            newRow = []
            print("\n")
            #soup.prettify(litag)
            #print(litag)
            for imgtag in litag.find_all("img"):
                #print ("image link = " + imgtag["src"])
                newRow.append(imgtag["src"])
                break
            #for productName in litag.find_all("a", {"class": "ProductDetails"}):
            #for productName in litag.find_all({"class": "ProductDetails"}):
            for productName in litag.find_all("div", {"class": "ProductDetails"}):
                #print("HELLO THERE " + "\n")
                #print ("product name = " + productName.find('a').text)
                #for prof in productName.find_all`
                name = productName.find('a').text
                newRow.append(name)
                result = (gettype(name))
                newRow.append(result[0])
                newRow.append(result[1])
                newRow.append(result[2])
                newRow.append(result[3])
                newRow.append(result[4])
                #print("product link: ")
                link = productName.find('a')
                newRow.append(link.get('href'))
                #print('\n' + 'name = ' + name)
            for productPrice in litag.find_all("div", {"class" : "ProductDetails"}):
                #print("price = " + productPrice.text)
                price = productPrice.find('em').text
                if not price:
                    price = "n/a"
                print('\n' + 'price in here = ' + price)
                newRow.append(getPrice(price))

            try:
                insertdb(newRow[0], newRow[7], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[8], "The Polo Shop")
            except IndexError:
                    print("product incomplete")
                    addError("the_polo_shop")



def thePoloShop():
    urlList = ["http://www.thepoloshop.co.uk/polo-basic-starter-kit/",
               "http://www.thepoloshop.co.uk/polo-boots/",
               "http://www.thepoloshop.co.uk/polo-belts/",
               "http://www.thepoloshop.co.uk/polo-helmets/",
               "http://www.thepoloshop.co.uk/polo-whites/",
               "http://www.thepoloshop.co.uk/club-clothing/",
               "http://www.thepoloshop.co.uk/bits/",
               "http://www.thepoloshop.co.uk/polo-boots-bandages/",
               "http://www.thepoloshop.co.uk/polo-tack-saddlery/?sort=newest&page=1",
               "http://www.thepoloshop.co.uk/polo-tack-saddlery/?sort=newest&page=2",
               "http://www.thepoloshop.co.uk/polo-equipment/",
               "http://www.thepoloshop.co.uk/vet-supplies/"
               ]


    print("\n" + "\n" + "Connecting to THE POLO SHOP WEBSITE" + "\n" + "\n")


    x = 0

    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getThePoloShopData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#thePoloShop()
