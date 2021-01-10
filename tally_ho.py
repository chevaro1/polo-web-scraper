import requests
from bs4 import BeautifulSoup
from config import insertdb
from get_html import getHTML, getSoup
from product_details import gettype
from get_price import getPrice


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       TALLY HO WEBSITE
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

list_of_rows =[]

def addRow(newRow):

    list_of_rows.append(newRow)

def getTallyHoData(soup):
        nameList = []
        priceList = []
        imgList = []
        linkList = []
        

        for divtag in soup.find_all("div", {"class": "priceoptions"}):
            #print (divtag.text)
            #price = formatText(divtag.text)
            price = divtag.text
            priceList.append(price)

        for nametag in soup.find_all("div", {"class": "name"}):
            for titletag in nametag.find_all("a"):
                    #print(titletag.text)
                    nameList.append(titletag.text)
        for phototag in soup.find_all("div", {"class": "thumb"}):
            link = phototag.find('a')
            #print("href")
            linkList.append("https://www.tallyhofarm.co.uk" + link.get('href'))
            for pictag in phototag.find_all("img"):
                #print (pictag["src"])
                #print("\n")
                imgList.append("https://www.tallyhofarm.co.uk" + pictag["src"])
                break

        x = 0

        while x < len(nameList):
            newRow = []
            
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
            
            addRow(newRow)
            x = x + 1
                
        #print("outputs: ", list_of_rows)


def upload():
    count = 0
    while count < len(list_of_rows):
        insertdb(list_of_rows[count][0],list_of_rows[count][1],list_of_rows[count][2],
                 list_of_rows[count][3],list_of_rows[count][4],list_of_rows[count][5],
                 list_of_rows[count][6],list_of_rows[count][7],list_of_rows[count][8],"tally_ho")
        count += 1




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
        upload()
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~" + "\n"
          + "PAGE IS FINISHED " + str(x) + "\n" + "~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

