import json
import os
from scrape import printData



sites = [#"naylors",
        #"discount_equestrian",
        #"equine_superstore",
        #"equus",
        #"hope_valley_saddlery",
        #"horze",
        #"online_for_equine",
        #"redpost_equestrian",
        "robinsons_equestrian"
        #"the_saddlery_shop",
        #"ayr_equestrian",
        #"derby_house_store",
        #"equestrian_world",
        #"equiport",
        #"houghton_country",      #cant seem to load all of the js  lazy loader problem scrapy-splash
        #"ingatestone_saddlery",    # fixed
        #"kramer",                  #need actual valid links otherwise working
        #"millbry_hill",              #lazy loader problem scrapy-splash
        #"randr_country",             # fixed
        #"royal_equestrian",
        #"shires_equestrian"
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

        print("key = " + key['link'])
        file = key['link']
        printData("https://www.robinsonsequestrian.com/brand/pikeur", yml)
        return

#        try:
#            print("key = " + key['link'])
#            file = key['link']
#            printData(file, yml)
#        except:
#            print("no products in link")

def scrapeMain():
    length = len(sites)
    count = 0
    while count < length:
        web = sites[count]
        print("website = " + web)
        getScraper(web)
        count += 1


scrapeMain()
