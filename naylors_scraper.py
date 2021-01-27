from selectorlib import Extractor
import requests
import os

def printData(sitelink):
    here = os.path.dirname(os.path.abspath(__file__))

    filename = os.path.join(here, 'naylors.yml')

    # Create an Extractor by reading from the YAML file
    e = Extractor.from_yaml_file(filename)

    # Download the page using requests
    #r = requests.get('https://www.naylors.com/women/country')
    #r = requests.get(file)

    # Pass the HTML of the page and create
    #data = e.extract(r.text)
    # Print the data
    #print(data)
    print("sitelink = " + sitelink)
    # Download another page of similar structure
    r = requests.get("naylors.json")
    #r = requests.get('https://www.naylors.com/')
    # Use the same extractor to get the data
    data = e.extract(r.text)
    # Print it again

    dist = data
    key = dist.keys()
    print("STARTING SCRAPE NOW")
    for x in dist:
      print(dist[x])
      print("hello there")
      print(x)
      for a in dist[x]:
        #print(a)
        print("\n" + "\n" + "inside: individual products" + "\n" + "\n")
        print("name = " + a["name"])
        print("price = " + a["price"])
        print("brand = " + a["brand"])
        print("product_link = " + a["product_link"])
        print("image = " + a["image"])
        #for i in a:
          #print(a[i])
          #print("inside: I")


printData("hi")
