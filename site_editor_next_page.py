#print("running next page")
#from scrape import printData
import re

def get_next(site, yml, sitelink):
    try:
        run = globals()[site]
        row = run(yml, sitelink)
    except:
        pass

def ingatestone_saddlery(yml, sitelink):
    maxpageno = 17

    x = re.findall("(?:[^\d]*(\d+)[^\d]*)+", sitelink)
    if len(x) == 0:
        page = "page/2/"
        sitelink = sitelink + page
    else:
        oldpg = x[0]
        pageno = int(x[0])
        pageno += 1
        if pageno > maxpageno:
            print("At end of pages")
            return
        page = str(pageno)
        #sitelink = re.sub("(?:[^\d]*(\d+)[^\d]*)+", page, sitelink)
        sitelink = re.sub(oldpg, page, sitelink)
        #print(sitelink)

    print("printdata below")
    from scrape import printData
    printData(yml, sitelink)
    print(sitelink)


def horze(yml, sitelink):
    maxpageno = 420

    x = re.findall("(?:[^\d]*(\d+)[^\d]*)+", sitelink)
    #print(x)
    if len(x) == 0:
        page = "?start=42"
        sitelink = sitelink + page
    else:
        oldpg = x[0]
        #print(oldpg)
        pageno = int(x[0])
        pageno += 42
        if pageno > maxpageno:
            print("At end of pages")
            return
        page = str(pageno)
        #sitelink = re.sub("(?:[^\d]*(\d+)[^\d]*)+", page, sitelink)
        sitelink = re.sub(oldpg, page, sitelink)
        #print(sitelink)

    print("site link = " + sitelink)
    from scrapejs import scrape
    scrape(yml, sitelink)





def test(yml, sitelink):
    maxpageno = 420

    x = re.findall("(?:[^\d]*(\d+)[^\d]*)+", sitelink)
    if len(x) == 0:
        page = "?start=42"
        sitelink = sitelink + page
    else:
        oldpg = x[0]
        pageno = int(x[0])
        pageno += 42
        if pageno > maxpageno:
            print("At end of pages")
            return
        page = str(pageno)
        #sitelink = re.sub("(?:[^\d]*(\d+)[^\d]*)+", page, sitelink)
        sitelink = re.sub(oldpg, page, sitelink)
        #print(sitelink)

    print(sitelink)
    #from scrape import printData
    printData(yml, sitelink)




#test("https://www.ingatestonesaddlery.co.uk/category/horse/saddlery-tack/page/10/")
#test("https://www.ingatestonesaddlery.co.uk/category/horse/saddlery-tack/")

#get_next("ingatestone_saddlery", "ingatestone_saddlery.yml", "https://www.ingatestonesaddlery.co.uk/category/horse/saddlery-tack/")
#get_next("horze", "horze.yml", "https://www.horze.co.uk/horse-rugs")
