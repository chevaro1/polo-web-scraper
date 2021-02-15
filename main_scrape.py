import json
import os
from scrape import printData
from multiprocessing import Pool
import gc


sites = ["naylors",
        "discount_equestrian",
        "equine_superstore",
        "equus",
        "hope_valley_saddlery",
        "horze",
        "online_for_equine",
        "redpost_equestrian",
        "robinsons_equestrian",
        "the_saddlery_shop",
        "ayr_equestrian",
        "derby_house_store",
        "equestrian_world",
        "equiport",
        "houghton_country",      #cant seem to load all of the js  lazy loader problem scrapy-splash
        "ingatestone_saddlery",    # fixed
        "kramer",                  #need actual valid links otherwise working
        "millbry_hill",              #lazy loader problem scrapy-splash
        "randr_country",             # fixed
        "royal_equestrian",
        "shires_equestrian",
        "imperial_equestrian",
        "equine_essentials_direct",
        "robinsons_equestrian_uk",
        "fast_tack_direct",
        "tack_shop",
        "dragonfly_saddlery",
        "equi_supermarket",
        "edgemere",
        "church_equestrian",
        "equiporium",
        "old_dairy_saddlery",
        "griggs_equestrian",
        "the_yard_equine",
        "the_ranch_store",
        "all_your_horse_needs",
        "throstlenest_saddlery",
        "just_equine",
        "rb_equestrian",
        "avily",
        "barnstaple_equestrian_supplies",
        "brendon_saddlery",
        "complete_equestrian",
        "cool_equestrian",
        "cork_farm_equestrian",
        "dash_equestrian",
        "denchworth_equestrian",
        "elite_saddlery",
        "equine_mania",
        "equitogs",
        "gilberts_equestrian",
        "hendry_equestrian_shop",
        "horse_and_rider",
        "just_horse_riders",
        "milton_equestrian",
        "oakfield_direct",
        "retford_saddlery",
        "saddlesdane",
        "smeeth_saddlery",
        "speedgate",
        "the_paddock_pantry",
        "wadswick"
        ]



def getScraper(site):

        sitelink = site + ".json"
        links = []

        here = os.path.dirname(os.path.abspath(__file__))

        filename = os.path.join(here, sitelink)

        with open(filename) as f:
            data = json.load(f)

        for key in data:
            temp = []
            temp.append(site + ".yml")
            temp.append(key["link"])
            links.append(temp)

        #print(links)

        #for i in links[:20]:
        #    scrape(i)

        #yyml = "horze"
        pool = Pool(processes=5)
        pool.starmap(printData, links)
        pool.close()
        pool.terminate()
        pool.join()


def scrapeMain(res):
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
        #getScraper(web)
        try:
            print("website = " + web)
            getScraper(web)
        except:
            print("website failed")
        count += 1

#res = ["naylors"]
#scrapeMain(res)
