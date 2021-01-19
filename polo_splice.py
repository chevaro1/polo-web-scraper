import requests

The following SQL statement selects all customers from the "Customers" table, sorted DESCENDING by the "Country" column:
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           POLOSPLICE WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getPoloSpliceData(soup):
    for ultag in soup.find_all('ul', {'class': 'productGrid'}):
        for litag in ultag.find_all('li'):
            newRow = []
            #print("\n")
            for imgtag in litag.find_all("img"):
                print (imgtag["src"])
                newRow.append(imgtag["src"])
            for productName in litag.find_all("h3", {"class": "card-title"}):
                #print (productName.text)
                name = productName.text
                newRow.append(name)
                result = (gettype(productName.text))
                newRow.append(result[0])
                newRow.append(result[1])
                newRow.append(result[2])
                newRow.append(result[3])
                newRow.append(result[4])
                print('\n' + 'name = ' + name)
                link = productName.find('a')
                newRow.append(link.get('href'))
            for productPrice in litag.find_all("span", {"class" : "price price--withTax"}):
                #print(productPrice.text)
                price = productPrice.text
                if not price:
                    price = "n/a"
                print('\n' + 'price = ' + price)
                newRow.append(getPrice(price))

            try:
                insertdb(newRow[0], newRow[7], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[8], "polo splice")
            except IndexError:
                    print("product incomplete")








def poloSplice():
    urlList = ["https://polosplice.co.uk/ona-polo/",
               "https://polosplice.co.uk/gift-items/",
               "https://polosplice.co.uk/hook-polo/",
               "https://polosplice.co.uk/instinct-polo-helmet-new-design/",
               "https://polosplice.co.uk/armis-polo-helmets/",
               "https://polosplice.co.uk/salvavita-polo-helmet/",
               "https://polosplice.co.uk/instinct-polo-helmet/",
               "https://polosplice.co.uk/horse-rugs/",
               "https://polosplice.co.uk/stable-yard-accessories/",
               "https://polosplice.co.uk/polo-mallets/",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=1",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=2",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=3",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=4",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=5",
               "https://polosplice.co.uk/player-accessories/?sort=newest&page=6",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=1",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=2",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=3",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=4",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=5",
               "https://polosplice.co.uk/horse-accessories/?sort=newest&page=6",
               "https://polosplice.co.uk/tack?sort=newest&page=1",
               "https://polosplice.co.uk/tack?sort=newest&page=2",
               "https://polosplice.co.uk/tack?sort=newest&page=3",
               "https://polosplice.co.uk/tack?sort=newest&page=4",
               "https://polosplice.co.uk/tack?sort=newest&page=5",
               "https://polosplice.co.uk/tack?sort=newest&page=6",
               "https://polosplice.co.uk/tack?sort=newest&page=7"
               ]


    print("\n" + "\n" + "Connecting to POLO SPLICE WEBSITE" + "\n" + "\n")


    x = 0

    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getPoloSpliceData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
