import json
import os
from scrapejs import scrape



res = ["millbry_hill",
       "horze",
       "oakfield_direct",
       "equine_essentials_direct",
       "equi_supermarket",
       "equine_superstore",
       "shires_equestrian"
        ]



def getScraper(site):

    sitelink = site + ".json"
    yml = site + ".yml"

    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, sitelink)

    with open(filename) as f:
        data = json.load(f)

    #print("yml = " + yml + "json = " + json)
    count = 0

    for key in data:
        count += 1

#        print("key = " + key['link'])
#        file = key['link']
#        printDataJs("https://www.horze.co.uk/stable-accessories", yml)
#        return

        try:
            print("key = " + key['link'])
            file = key['link']
            printDataJs(file, yml)
        except:
            print("no products in link")

#def scrapeMain(res):
def scrapeMainJs():
    #res = ["horze"]
    length = len(res)
    count = 0
    while count < length:
        web = res[count]
        #getScraper(web)
        try:
            print("website = " + web)
            getScraper(web)
        except:
            print("website failed")
        count += 1

def scrapeSingle(res):
    length = len(res)
    count = 0
    while count < length:
        web = res[count]
        try:
            print("website = " + web)
            getScraper(web)
        except:
            print("website failed")
        count += 1

#res = ["millbry_hill"]
scrapeMainJs()

#scrape("horze.yml", "https://www.horze.co.uk/horse-rugs?start=252")
