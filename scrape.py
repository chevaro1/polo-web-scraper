from selectorlib import Extractor
import requests
import os
from config import insertdb
from product_details import gettype
from get_price import getPrice
from errors import addError

def printData(sitelink, yml):
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, yml)

    # Create an Extractor by reading from the YAML file
    e = Extractor.from_yaml_file(filename)

    site = yml[:-4]
    print("SITE = " + site)

    # Download the page using requests
    #r = requests.get('https://www.naylors.com/women/country')
    #r = requests.get(file)

    #print("web page = " + sitelink)
    # Pass the HTML of the page and create
    #data = e.extract(r.text)
    # Print the data
    #print(data)
    #print("sitelink = " + sitelink)
    # Download another page of similar structure
    r = requests.get(sitelink, timeout=5)
    #r = requests.get('https://www.naylors.com/')
    # Use the same extractor to get the data
    data = e.extract(r.text)
    # Print it again

    dist = data
    key = dist.keys()
    print("SCRAPING NEW WEBSITE")
    for x in dist:
      #print(dist[x])
      #print("hello there")
      #print(x)
      for a in dist[x]:
        newRow = []
        #print(a)
        print("\n" + "\n")
        print("\n" + "\n" + "inside: individual product" + "\n" + "\n")
        newRow.append(a["image"])
        print("name = " + a["name"])
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
        print(newRow)
        try:
            insertdb(newRow[0], newRow[7], newRow[1], newRow[2], newRow[3], newRow[4], newRow[5], newRow[6], newRow[8], site)
        except IndexError:
            print("product incomplete")
            addError(site)



#printData("hi")
