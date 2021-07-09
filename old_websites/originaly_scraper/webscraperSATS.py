import requests
from bs4 import BeautifulSoup
import csv

def getHTML(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    print("request complete")
    return response.content

def getSoup(html):
    soup = BeautifulSoup(html, "html.parser")
    #print (soup.prettify())
    return soup

def formatText(text):
    text = text.replace("\n", "")
    text = text.replace("\t", "")
    text = text.replace("\r", "")
    text = text.replace("inc VAT", "")
    text = text.replace("SmallMediumLarge", "")
    text = text.replace("(VAT exempt)", "")
    text = text.replace("Price:", "")
    text = text.replace("from:", "")
    text = text.replace("from", "")
    text = text.rstrip()
    text = text.lstrip()
    text = text.split()[0]
     
    return text
    

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       CSV WRITER
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

list_of_rows =[]

def addRow(newRow):

    list_of_rows.append(newRow)


def printListOfRows():
    print(list_of_rows)





def createCSV():
    print("createCSV started")
    outfile = open("./Data.csv", "w")
    writer = csv.writer(outfile)
    writer.writerows(list_of_rows)
    print("action finished")













#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       SATS POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getSatsPoloData(soup):
    for ultag in soup.find_all('ul', {'class': 'products columns-4'}):
        for litag in ultag.find_all('li'):
            newRow = []
            #print("\n")
            for imgtag in litag.find_all("img"):
                #print (imgtag["src"])
                newRow.append(imgtag["src"])
            for productName in litag.find_all("h2", {"class": "woocommerce-loop-product__title"}):
                #print (productName.text)
                newRow.append(productName.text)
            for productPrice in litag.find_all("span", {"class" : "price"}):
                #print(productPrice.text)
                newRow.append(productPrice.text)

            addRow(newRow)        

def SatsPolo():
    urlList = ["https://www.satsfaction.com/shop/page/1/",
        "https://www.satsfaction.com/shop/page/2/",
        "https://www.satsfaction.com/shop/page/3/",
        "https://www.satsfaction.com/shop/page/4/",
        "https://www.satsfaction.com/shop/page/5/",
        "https://www.satsfaction.com/shop/page/6/",
        "https://www.satsfaction.com/shop/page/7/",
        "https://www.satsfaction.com/shop/page/8/",
        "https://www.satsfaction.com/shop/page/9/"]

    print("\n" + "\n" + "Connecting to SATS POLO WEBSITE" + "\n" + "\n")


    for i in urlList:
        HTML = getHTML(i)
        soup = getSoup(HTML)
        getSatsPoloData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + i + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           RJPOLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getRJPoloData(soup):
        for ultag in soup.find_all('ul', {'class': 'product-list list-reset'}):
            for litag in ultag.find_all('li'):
                #print("\n")
                newRow = []
                for imgtag in litag.find_all("img"):
                    print ("https://www.rjpolo.com/" + imgtag["src"])
                    newRow.append("https://www.rjpolo.com" + imgtag["src"])
                for productName in litag.find_all("h2", {"class": "product-item-title ib-m"}):
                    print (productName.text)
                    name = productName.text
                    newRow.append(name)
                for productPrice in litag.find_all("div", {"class" : "product-price ib-m"}):
                    print(productPrice.text)
                    price = formatText(productPrice.text)
                    newRow.append(price)
                addRow(newRow)

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
        



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       TALLY HO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getTallyHoData(soup):
        nameList = []
        priceList = []
        imgList = []
        

        for divtag in soup.find_all("div", {"class": "priceoptions"}):
            #print (divtag.text)
            price = formatText(divtag.text)
            priceList.append(price)

        for nametag in soup.find_all("div", {"class": "name"}):
            for titletag in nametag.find_all("a"):
                    #print(titletag.text)
                    nameList.append(titletag.text)
        for phototag in soup.find_all("div", {"class": "thumb"}):
            for pictag in phototag.find_all("img"):
                #print (pictag["src"])
                #print("\n")
                imgList.append("https://www.tallyhofarm.co.uk" + pictag["src"])
                break

        x = 0

        while x < len(nameList):
            newRow = []
            
            newRow.append(imgList[x])
            newRow.append(nameList[x])
            newRow.append(priceList[x])
            
            addRow(newRow)
            x = x + 1
                
        print("outputs: ", list_of_rows)

def TallyHo():
    urlList = ["https://www.tallyhofarm.co.uk/polo-equipment/c29?page=5",
               "https://www.tallyhofarm.co.uk/polo-equipment/c29?page=4",
               "https://www.tallyhofarm.co.uk/polo-equipment/c29?page=3",
               "https://www.tallyhofarm.co.uk/polo-equipment/c29?page=2",
               "https://www.tallyhofarm.co.uk/polo-equipment/c29?page=1"]


    print("\n" + "\n" + "Connecting to TALLY HO WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getTallyHoData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           CASABLANCA WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getCasablancaData(soup):
    print("entered get data")
    for divtag in soup.find_all("div", {"class": "category-products"}):
        for ultag in divtag.find_all('ul'):
            #print(ultag)
            for litag in ultag.find_all('li'):
                print("\n")
                newRow = []
                for imgtag in litag.find_all("img", {"class" : "product-main-photo"}):
                    #print ("img source: " + imgtag["src"])
                    newRow.append(imgtag["src"])
                for productName in litag.find_all("h5"):
                    #print ("product name: " + productName.text)
                    name =(productName.text)
                    newRow.append(name)
                for productPrice in litag.find_all("div", {"class" : "price-box"}):
                    #print("product price: " + productPrice.text)
                    price = formatText(productPrice.text)
                    newRow.append(price)
                addRow(newRow)



def Casablanca():
    urlList = ["https://www.casablancapolo.com/unitedkingdom/saddles",
               "https://www.casablancapolo.com/unitedkingdom/helmet#",
               "https://www.casablancapolo.com/unitedkingdom/boots",
               "https://www.casablancapolo.com/unitedkingdom/kneeguards",
               "https://www.casablancapolo.com/unitedkingdom/gloves",
               "https://www.casablancapolo.com/unitedkingdom/polo-elbow-pads",
               "https://www.casablancapolo.com/unitedkingdom/base-layers",
               "https://www.casablancapolo.com/unitedkingdom/accessory",
               "https://www.casablancapolo.com/unitedkingdom/whips",
               "https://www.casablancapolo.com/unitedkingdom/saddle-fittings",
               "https://www.casablancapolo.com/unitedkingdom/bridles",
               "https://www.casablancapolo.com/unitedkingdom/polo-balls",
               "https://www.casablancapolo.com/unitedkingdom/bags",
               "https://www.casablancapolo.com/unitedkingdom/t-shirts",
               "https://www.casablancapolo.com/unitedkingdom/polos",
               "https://www.casablancapolo.com/unitedkingdom/shirts",
               "https://www.casablancapolo.com/unitedkingdom/knits",
               "https://www.casablancapolo.com/unitedkingdom/jackets-outerwear",
               "https://www.casablancapolo.com/unitedkingdom/trousers",
               "https://www.casablancapolo.com/unitedkingdom/leather-goods",
               "https://www.casablancapolo.com/unitedkingdom/accessories",
               "https://www.casablancapolo.com/unitedkingdom/women"
               ]


    print("\n" + "\n" + "Connecting to CASABLANCA WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getCasablancaData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           POLOSPLICE WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getPoloSpliceData(soup):
    for ultag in soup.find_all('ul', {'class': 'productGrid'}):
        for litag in ultag.find_all('li'):
            newRow = []
            #print("\n")
            for imgtag in litag.find_all("img"):
                #print (imgtag["src"])
                newRow.append(imgtag["src"])
            for productName in litag.find_all("h4", {"class": "card-title"}):
                #print (productName.text)
                name = formatText(productName.text)
                newRow.append(name)
            for productPrice in litag.find_all("span", {"class" : "price price--withTax"}):
                #print(productPrice.text)
                price = formatText(productPrice.text)
                newRow.append(price)

            addRow(newRow)



    




def poloSplice():
    urlList = [#"https://polosplice.co.uk/ona-polo/",
               #"https://polosplice.co.uk/gift-items/",
               #"https://polosplice.co.uk/hook-polo/",
               #"https://polosplice.co.uk/instinct-polo-helmet-new-design/",
               #"https://polosplice.co.uk/armis-polo-helmets/",
               #"https://polosplice.co.uk/salvavita-polo-helmet/",
               #"https://polosplice.co.uk/instinct-polo-helmet/",
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






#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           PORTO POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getPortoPoloData(soup):
        nameList = []
        priceList = []
        imgList = []
        

        for divtag in soup.find_all("div", {"class": "prodprice"}):
            #print (divtag.text)
            price = formatText(divtag.text)
            priceList.append(price)

        for nametag in soup.find_all("div", {"class": "prodname"}):
            for titletag in nametag.find_all("a"):
                    #print(titletag.text)
                    nameList.append(titletag.text)
        for phototag in soup.find_all("div", {"class": "prodimage allprodimages"}):
            for pictag in phototag.find_all("img"):
                #print (pictag["src"])
                #print("\n")
                imgList.append("https://portopolo.com/" + pictag["src"])
                break

        x = 0

        while x < len(nameList):
            newRow = []
            
            newRow.append(imgList[x])
            newRow.append(nameList[x])
            newRow.append(priceList[x])
            
            addRow(newRow)
            x = x + 1
                




def PortoPolo():
    urlList = ["https://portopolo.com/products.php?cat=Bridleware+%26+Bits"]


    print("\n" + "\n" + "Connecting to PORTO POLO WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getPortoPoloData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")







#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           LA MARTINA WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



def getLaMartinaData(soup):
        nameList = []
        priceList = []
        imgList = []
        
        #PRICE
        for pricetag in soup.find_all("span", {"class": "price-value-int"}):
            #print (pricetag.text)
            price = formatText(pricetag.text)
            priceList.append(price)

        
        #NAME
        for nametag in soup.find_all("span", {"class": "prd-name"}):
            #for titletag in nametag.find_all("a"):
            #print(nametag.text)
            nameList.append(nametag.text)

        #IMAGE            
        for phototag in soup.find_all("picture"):
            for pictag in phototag.find_all("img"):
                #print (pictag["src"])
                #print("\n")
                imgList.append("https://www.lamartina.com/" + pictag["src"])
                break

        x = 0

        while x < len(nameList):
            newRow = []
            
            newRow.append(imgList[x])
            newRow.append(nameList[x])
            newRow.append(priceList[x])
            
            addRow(newRow)
            x = x + 1
                




def LaMartina():
    urlList = ["https://www.lamartina.com/lm/gb/en/Categories/Technical-Equipment/c/TE"]


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




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           WORLD WIDE TACK WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getWorldWideTackData(soup):
        nameList = []
        priceList = []
        imgList = []
        
        #PRICE
        for pricetag in soup.find_all("span", {"class": "woocommerce-Price-amount amount"}):
            #print ("price: " + pricetag.text)
            price = formatText(pricetag.text)
            priceList.append(price)

        
        #NAME
        for nametag in soup.find_all("div", {"class": "whiteBox"}):
            for titletag in nametag.find_all("h2"):
                print("name: " + titletag.text)
                name = titletag.text
                #name.strip('"')
                nameList.append(name)
                

        #IMAGE            
        for phototag in soup.find_all("a", {"class": "imageContainer"}):
            for pictag in phototag.find_all("img"):
                #print ("img scr: " + pictag["src"])
                #print("\n")
                imgList.append(pictag["src"])
                break

        x = 0

        while x < len(nameList):
            newRow = []
            
            newRow.append(imgList[x])
            newRow.append(nameList[x])
            newRow.append(priceList[x])
            
            addRow(newRow)
            x = x + 1
                




def WorldWideTack():
    urlList = ["https://www.worldwidetack.com/category/polo-equipment/polo-accessories/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-bits/4-rings/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-bits/3-rings/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-bits/big-ring-gags/",
               "https://www.worldwidetack.com/category/polo-equipment/polo-bits/pelhams/",
               #"https://www.worldwidetack.com/category/polo-equipment/polo-leatherwork/"
               ]


    print("\n" + "\n" + "Connecting to WORLD WIDE TACK WEBSITE" + "\n" + "\n")


    x = 0
    
    for i in urlList:
        x += 1
        HTML = getHTML(i)
        #print("hello")
        soup = getSoup(HTML)
        getWorldWideTackData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")




#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           THE POLO SHOP WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getThePoloShopData(soup):
    for ultag in soup.find_all('ul', {'class': 'ProductList'}):
        for litag in ultag.find_all('li'):
            newRow = []
            print("\n")
            for imgtag in litag.find_all("img"):
                print (imgtag["src"])
                newRow.append(imgtag["src"])
                break
                
            for productName in litag.find_all("div", {"class": "ProductDetails"}):
                for name in productName.find_all("a"):
                    newRow.append(name.text)   
                    print (name.text)
                    
            for productPrice in litag.find_all("div", {"class" : "ProductDetails"}):
                for price in productPrice.find_all("em"):
                    if len(price.text) > 7 :
                        finPrice = price.text
                        finPrice = finPrice[7:]
                        print(finPrice)
                        newRow.append(finPrice)
                    else:
                        print(price.text)
                        newRow.append(price.text)

            addRow(newRow)        

def ThePoloShop():
    urlList = ["http://www.thepoloshop.co.uk/polo-basic-starter-kit/",
               "http://www.thepoloshop.co.uk/polo-tack-saddlery/?sort=newest&page=2",
               "http://www.thepoloshop.co.uk/polo-tack-saddlery/?sort=newest&page=1",
               "http://www.thepoloshop.co.uk/polo-boots-bandages/",
               "http://www.thepoloshop.co.uk/bits/",
               "http://www.thepoloshop.co.uk/polo-belts/",
               "http://www.thepoloshop.co.uk/polo-helmets/",
               "http://www.thepoloshop.co.uk/polo-whites/",
               "http://www.thepoloshop.co.uk/polo-equipment/"
               ]

    print("\n" + "\n" + "Connecting to THE POLO SHOP WEBSITE" + "\n" + "\n")


    for i in urlList:
        HTML = getHTML(i)
        soup = getSoup(HTML)
        getThePoloShopData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + i + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           DISCOUNT EQUESTRIAN WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def getDiscountEquestrianData(soup):
    for oltag in soup.find_all('ol', {'class': 'products list items product-items'}):
        for litag in oltag.find_all('li'):
            newRow = []
            print("\n")
            for imgtag in litag.find_all("img"):
                print (imgtag["src"])
                newRow.append(imgtag["src"])
                break
                
            for productName in litag.find_all("strong", {"class": "product name product-item-name"}):
                for name in productName.find_all("a"):
                    newRow.append(name.text)   
                    print (name.text)
                    
            for productPrice in litag.find_all("span", {"class" : "normal-price"}):
                for price in productPrice.find_all("span", {"class" : "price"}):
                    print(price.text)
                    newRow.append(price.text)

            addRow(newRow)        



def DiscountEquestrian():
    urlList = ["https://www.discount-equestrian.co.uk/horse/horse-wear/polo-equipment.html?stock=1&p=1",
               "https://www.discount-equestrian.co.uk/horse/horse-wear/polo-equipment.html?stock=1&p=2",
               "https://www.discount-equestrian.co.uk/horse/horse-wear/polo-equipment.html?stock=1&p=3",
               ]

    print("\n" + "\n" + "Connecting to DISCOUNT EQUESTRIAN WEBSITE" + "\n" + "\n")


    for i in urlList:
        HTML = getHTML(i)
        soup = getSoup(HTML)
        getDiscountEquestrianData(soup)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + i + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           ROXTONS WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~












#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           WP POLO GEAR WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~












#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           HORSE AND HOOF WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~











#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           PERFORMANCE POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~










#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           CALCUTT & SONS WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~











#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           NEWMARKET STABLECARE WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~







# WEBSITE NAME SUGGESTIONS: CLUB-CHUKKA , chukka club

#TallyHo()
#SatsPolo()
#RJPolo()
#Casablanca()
poloSplice()
#PortoPolo()
#LaMartina()
#WorldWideTack()
#ThePoloShop()
#DiscountEquestrian()
printListOfRows()
#createCSV()

print("\n" + "\n" + "Download Complete")
