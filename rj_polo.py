import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice
from errors import addError


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           RJPOLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getRJPoloData(soup):
        print("inside rj data")
        for ultag in soup.find_all('ul', {'class': 'product-list list-reset'}):
            for litag in ultag.find_all('li'):
                #print("\n")
                newRow = []
                for imgtag in litag.find_all("img"):
                    #print ("https://www.rjpolo.com/" + imgtag["src"])
                    #newRow.append("https://www.rjpolo.com" + imgtag["src"])
                    newRow.append(imgtag["src"])
                for productName in litag.find_all("h2", {"class": "product-item-title ib-m"}):
                    #print (productName.text)
                    name = productName.text
                    newRow.append(name)
                    result = (gettype(productName.text))
                    newRow.append(result[0])
                    newRow.append(result[1])
                    newRow.append(result[2])
                    newRow.append(result[3])
                    newRow.append(result[4])
                    #print("product link: ")
                    link = productName.find('a')
                    newRow.append("https://www.rjpolo.com/" + link.get('href'))
                for productPrice in litag.find_all("div", {"class" : "product-price ib-m"}):
                    #print(productPrice.text)
                    price = productPrice.text.strip()
                    newRow.append(getPrice(price))
                try:
                    insertdb(newRow[0], newRow[7], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[8], "RJ_Polo")
                except IndexError:
                        print("product incomplete")
                        addError("rj polo")

def RJPolo():
    urlList = ["https://www.rjpolo.com/instinct-polo-helmets-70-c.asp",
               "https://www.rjpolo.com/polo-helmet--faceguards-21-c.asp",
               "https://www.rjpolo.com/oakley-glasses-69-c.asp",
               "https://www.rjpolo.com/polo-goggles-27-c.asp",
               "https://www.rjpolo.com/polo-boots--spurs-22-c.asp",
               "https://www.rjpolo.com/rj-polo-bags-30-c.asp",
               "https://www.rjpolo.com/polo-clothing-and-polo-white-jeans-26-c.asp",
               "https://www.rjpolo.com/polo-kneepads-64-c.asp",
               "https://www.rjpolo.com/polo-elbow-pads-23-c.asp",
               "https://www.rjpolo.com/polo-gloves--wrist-supports-24-c.asp",
               "https://www.rjpolo.com/polo-mallets--balls-28-c.asp",
               "https://www.rjpolo.com/polo-whips-25-c.asp",
               "https://www.rjpolo.com/argentine-polo-belts-49-c.asp",
               "https://www.rjpolo.com/rj-polo-bundles-50-c.asp",
               "https://www.rjpolo.com/bomber-bits-62-c.asp",
               "https://www.rjpolo.com/polo-saddles--fittings-40-c.asp",
               "https://www.rjpolo.com/polo-bridles-32-c.asp",
               "https://www.rjpolo.com/polo-bits-33-c.asp",
               "https://www.rjpolo.com/polo-boots-bandages-headcollars-kit--tack-bags-34-c.asp",
               "https://www.rjpolo.com/cirencester-park-polo-club-clothing-82-c.asp",
               "https://www.rjpolo.com/argentine-dog-collars-and-leads-80-c.asp",
               "https://www.rjpolo.com/polo-belts-79-c.asp",
               "https://www.rjpolo.com/polo-stable--vet-supplies-17-c.asp",
               "https://www.rjpolo.com/a-selection-of--polo-sheets-and-polo-rugs-for-your-horse-37-c.asp",
               "https://www.rjpolo.com/various-polo-equipment---a-selection-of-polo-items-for-your-horse-from-studs-to-pads-38-c.asp"
               ]
    print("\n" + "\n" + "Connecting to RJ POLO WEBSITE" + "\n" + "\n")


    x = 0

    for i in urlList:
        x += 1
        HTML = getHTML(i)
        soup = getSoup(HTML)
        getRJPoloData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
