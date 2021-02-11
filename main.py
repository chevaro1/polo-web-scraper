from sats_polo import SatsPolo
from rj_polo import RJPolo
from tally_ho import TallyHo
from casablanca import Casablanca
from polo_splice import poloSplice
from porto_polo import PortoPolo
from la_martina import LaMartina
from world_wide_tack import WorldWideTack
from the_polo_shop import thePoloShop
from delete_duplicate import deleteDup
from roxtons import roxtons
from ona_polo import onaPolo
from performance_polo import PerformancePolo
from willoughby_park import WilloughbyPark
from krono_polo import KronoPolo
from truncate_db import truncate
from get_active import get_active
from errors import saveErrorLog
from main_scrape import scrapeMain
from scrapejs import runscrape

print("Application running")
truncate()
print("database cleared")

res = get_active()
print(res)
for x in res:
    try:
        run = globals()[x]
        run()
        res.remove(x)
    except:
        print("invalid website")


scrapeMain(res)
runscrape()

#SatsPolo()
#RJPolo()
#TallyHo()
#Casablanca()
#poloSplice()
#PortoPolo()
#LaMartina()
#WorldWideTack()
#thePoloShop()
#roxtons()
#onaPolo()
#PerformancePolo() THIS DOES NOT WORK, KEEP COMMENTED OUT
#WilloughbyPark()
#KronoPolo()


print("deleting duplicates")
deleteDup()

print("saving error log")
saveErrorLog()

print("application complete")



# to do list
# performance polo : https://www.performance-polo.com/shop DOESNT WORK
# hurlingham polo : www.hurlinghampolo1875.com NOT WORTH IT
