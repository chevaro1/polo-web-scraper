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

print("Application running")
truncate()
print("database cleared")

SatsPolo()
RJPolo()
TallyHo()
Casablanca()
poloSplice()
PortoPolo()
LaMartina()
WorldWideTack()
thePoloShop()
roxtons()
onaPolo()
#PerformancePolo() THIS DOES NOT WORK, KEEP COMMENTED OUT
WilloughbyPark()
KronoPolo()


print("deleting duplicates")
deleteDup()

print("application complete")


# to do list
# performance polo : https://www.performance-polo.com/shop DOESNT WORK
# hurlingham polo : www.hurlinghampolo1875.com NOT WORTH IT

