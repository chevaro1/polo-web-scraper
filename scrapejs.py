from multiprocessing import Pool
from requests_html import HTMLSession
from selectorlib import Extractor
import os
import json
from config import insertdb
from product_details import gettype
from get_price import getPrice
from errors import addError
from site_editor import clean_up
import re



#yml = "horze.yml"


def scrape(yml, link):
        #print(yml + link)
        #link = [links[0][1]]
        #yml = [links[0][0]]
    try:
        here = os.path.dirname(os.path.abspath(__file__))

        filename = os.path.join(here, yml)

        # Create an Extractor by reading from the YAML file
        e = Extractor.from_yaml_file(filename)

        site = yml[:-4]
        print("SITE = " + link)

        # Download the page using requests
        #r = requests.get('https://www.naylors.com/women/country')
        #r = requests.get(file)
        session = HTMLSession()
        #print("web page = " + sitelink)
        # Pass the HTML of the page and create
        #data = e.extract(r.text)
        # Print the data
        #print(data)
        #print("sitelink = " + sitelink)
        # Download another page of similar structure
        r = session.get(link, timeout=17)
        #r = session.get("https://www.millbryhill.co.uk/global-herbs-m1", timeout=17)
        r.html.render(retries=3, wait=5, timeout=20, scrolldown=10)
        #r = requests.get(sitelink)
        #r = requests.get('https://www.naylors.com/')
        # Use the same extractor to get the data
        #print(r.text)
        data = e.extract(r.text)
        # Print it again
        #print(r.text)
        session.close()
        dist = data
        key = dist.keys()
        print("SCRAPING NEW WEBSITE")
        for x in dist:
          #print(dist[x])
          #print("hello there")
          #print(x)
          try:
              for a in dist[x]:
                  try:
                    newRow = []
                    #print(a)
                    #print("\n" + "\n")
                    #print("\n" + "\n" + "inside: individual product" + "\n" + "\n")
                    newRow.append(a["image"])
                    #print("name = " + a["name"])
                    #print("price = " + a["price"])
                    #print("product_link = " + a["product_link"])
                    #print("image = " + a["image"])
                    name = a["name"].strip()
                    newRow.append(name)
                    result = (gettype(name))
                    newRow.append(result[0])
                    newRow.append(result[1])
                    newRow.append(result[2])
                    newRow.append(result[3])
                    newRow.append(result[4])
                    newRow.append(a["product_link"].strip())
                    price = "n/a"
                    price = a["price"].strip()
                    newRow.append(getPrice(price))
                    newRow = clean_up(site, newRow)

                    #print(newRow)
                    insertdb(newRow[0], newRow[7], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[8], site)
                  except:
                    print("invalid product")
          except:
              print("no products in page")

        #if(site == "millbry_hill" & re.search("^page=[0-9]", link[-6:]) & link[-1:] != 3):
        #    linkno = int(link[-1:]) + 1
        #    newlink = link[-1:] + linkno
        #    scrape(yml,newlink)

    except:
        print("couldnt load page")
        session.close()





def launchsite(site):
    #site = "horze"
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
    pool = Pool(processes=5, maxtasksperchild=1)
    pool.starmap(scrape, links[:10])
    pool.close()
    pool.terminate()
    pool.join()


lil = ["millbry_hill",
       "horze",
       "oakfield_direct",
       "equine_essentials_direct",
       "equi_supermarket",
       "equine_superstore",
       "shires_equestrian"
       ]
def runscrape():
    for i in lil:
        print("launching site")
        launchsite(i)
    #break
#launchsite("millbry_hill")
#runscrape()
