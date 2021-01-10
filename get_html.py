import requests
from bs4 import BeautifulSoup


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                       GET HTML
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def getHTML(url):
    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    print("request complete")
    return response.content

def getSoup(html):
    soup = BeautifulSoup(html, "html.parser")
    #print (soup.prettify())
    return soup
