import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice
from errors import addError

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                           PORTO POLO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getPortoPoloData(soup):
        nameList = []
        priceList = []
        imgList = []
        linkList = []


        for divtag in soup.find_all("div", {"class": "prodprice"}):
            #print (divtag.text)
            price = divtag.text
            priceList.append(price)

        for nametag in soup.find_all("div", {"class": "prodname"}):
            link = nametag.find('a')
            #print("href")
            linkList.append("https://portopolo.com/" + link.get('href'))

            for titletag in nametag.find_all("a"):
                    #print(titletag.text)
                    nameList.append(titletag.text)
        for phototag in soup.find_all("div", {"class": "prodimage allprodimages"}):
            for pictag in phototag.find_all("img"):
                #print (pictag["src"])
                #print("\n")
                imgList.append("https://portopolo.com/" + pictag["src"])
                #imgList.append(pictag["src"])
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


                insertdb(newRow[0], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[7], newRow[8], "porto polo")
            except IndexError:
                    print("product incomplete")
                    addError("porto polo")
            x = x + 1





def PortoPolo():
    urlList = ["https://portopolo.com/search.php?nobox=&scat=&pg=2",
               "https://portopolo.com/search.php?nobox=&scat=&pg=2",
               "https://portopolo.com/search.php?nobox=&scat=&pg=3",
               "https://portopolo.com/search.php?nobox=&scat=&pg=4",
               "https://portopolo.com/search.php?nobox=&scat=&pg=5",
               "https://portopolo.com/search.php?nobox=&scat=&pg=6",
               "https://portopolo.com/search.php?nobox=&scat=&pg=7",
               "https://portopolo.com/search.php?nobox=&scat=&pg=8",
               "https://portopolo.com/search.php?nobox=&scat=&pg=9",
               "https://portopolo.com/search.php?nobox=&scat=&pg=10",
               "https://portopolo.com/search.php?nobox=&scat=&pg=11",
               "https://portopolo.com/search.php?nobox=&scat=&pg=12",
               "https://portopolo.com/search.php?nobox=&scat=&pg=13",
               "https://portopolo.com/search.php?nobox=&scat=&pg=14",
               "https://portopolo.com/search.php?nobox=&scat=&pg=15"
                ]


    print("\n" + "\n" + "Connecting to PORTO POLO WEBSITE" + "\n" + "\n")


    x = 0

    for i in urlList:
        x += 1
        try:
            HTML = getHTML(i)
            #print("hello")
            soup = getSoup(HTML)
            getPortoPoloData(soup)
        except:
            print("could not connect to webpage")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
