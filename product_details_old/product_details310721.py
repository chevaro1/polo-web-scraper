
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      WEIGHTING
#                   0 = LOW WEIGHTING (COMMON NAME)
#                   5 = HIGH WEIGHTING (VERY UNCOMMON)(MUST BE THIS IF NAME IS INCLUDED)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



categories = {"bag": [["whip bag", 4], ["jodhpur boot bag", 4], ["riding bootbag", 4], ["boot bag", 4], ["hat bag", 4], ["helmet bag", 4], ["mallet bag", 4], ["saddle bag", 4], ["bag", 1], ["luggage", 4],
              ["kit bag", 4], ["bridle bag", 5], ["stick bag", 4], ["tack bag", 4], ["bandage bag", 4]],
              "horseboot": [["circulation hoof sock", 4], ["fetlock sock", 4], ["mud sock", 4], ["hoof sock", 4], ["equi-chaps", 4], ["covalliero soft gaiters", 4], ["scoot boot", 4], ["easyboot", 5], ["mud fever boot", 4], ["hybrid boot", 3], ["compression boot", 3], ["procool", 3], ["luxury protection boot", 4], ["woof ultra boot", 4], ["schooling boot", 4], ["hoof gel boot", 4], ["hydro boot", 3], ["brushing boot", 3], ["fetlock boot", 3], ["travel boot", 4], ["skid boot", 3], ["sports boot", 3], ["bell boot", 3], ["leg boot", 4], ["event boot", 3], ["reflective boot", 3], ["tendon boot", 4], ["stable protection boot", 4], ["relief boot", 4], ["soaking boot", 4], ["air flow boot", 4], ["fetlock vent boot", 4], ["fetlock protection boot", 4], ["fly boot", 4], ["flyboot", 4], ["club boot", 3], ["grafter boot", 3], ["exercise boot", 3], ["knee boot", 3], ["shipping boot", 3], ["cross country boot", 4], ["pastern", 4], ["poultice", 4], ["pastern wrap", 4], ["pastern boot", 4], ["tendon boot", 3], ["magnetic chaps", 4], ["equi-chaps, close contact", 4], ["equi-chaps close contact", 4], ["close contact chaps", 4], ["stable chaps", 3], ["hardy chaps", 3], ["support boot", 3], ["ice boot", 3], ["magnetic boot", 3], ["therapeutic support boot", 3], ["aero magneto", 3], ["ice vibe", 4], ["ice-vibe", 4], ["magnetik", 3], ["hock boot", 3], ["dressage boot", 4], ["splint boot", 3], ["hoof boot", 3], ["front boot", 3], ["reach boot", 3], ["horse boot", 3], ["travel boot", 3], ["travelling boot", 3], ["hing boot", 3], ["poultice boot", 3], ["ballistic", 4], ["over reach", 3], ["tendon", 3], ["Racing Tack replacement straps", 4], ["sport boot", 3], ["freeze boot", 3], ["therapy boot", 3], ["magno boot", 3], ["veredus", 3], ["kentucky horsewear", 4], ["christ boot", 3], ["stable boot", 3], ["skid boot", 3], ["sports boot", 2], ["sports medicine boot", 4], ["bell boot", 4], ["fetlock boot", 3], ["jump boot", 3], ["brushing boot", 3], ["overreach boot", 3], ["fetlock ring", 2]],
              "poloboot": [["twin gore", 3], ["polo boot", 2], ["layer boot", 2], ["boot", 1], ["jodhpur boot", 5]],
              "ridingboot":[["aspen boot", 4], ["riding boot", 3], ["ariat barn", 4], ["twin gore", 3], ["polo boot", 2], ["layer boots", 2], ["boot", 1], ["jodhpur childrens boot", 4], ["jodhpur boot", 4]],
			  "countryboot":[["country boot", 3]],
			  "dressageboot":[],
			  "yardboot": [["skyline summit", 4], ["skyline summit", 4], ["chainsaw boot", 5], ["telluride", 4], ["terrain zip", 4], ["ariat terrain", 4], ["frostline", 3], ["mudbuster", 4], ["mont blanc winter", 4], ["mont blanc winter", 4], ["hercules lace-up", 4], ["muds", 4], ["safety boot", 4], ["wester boot", 4], ["yardmaster boot", 4], ["yardmaster tall boot", 4], ["frost boot", 5], ["muddies", 5], ["hkm davos", 4], ["muck boot", 4], ["mucker boot", 4], ["rain boot", 4], ["rainboot", 4], ["yardboot", 4], ["yard boot", 4]],
			  "boot_maintenance": [["boot shine",3], ["boot wax", 3], ["boot miracle", 4], ["boots cleaner", 4]],
			  "footwear":[["fairfax & favor", 4], ["burnham", 3], ["regina suede", 3], ["walking boot", 4], ["ladies langham", 4], ["hiking", 3], ["chelsea boot, 4"], ["slippers, 4"]],
			  "ball": [["jolly ball", 3], ["horsemens pride jolly ball", 4], ["stable  toy", 4], ["carrot ball", 3], ["horse playball", 3], ["snak-a-ball", 4], ["hay ball", 3], ["hayball", 3], ["wash ball", 3], ["feeder ball", 3], ["ball feeder", 3], ["treat ball", 3], ["hangin' ball", 4], ["equine play ball", 4], ["carrot ball", 3]],
              "polo_ball": [["polo ball", 3], ["umpire ball bag", 4], ["ball bag", 3]],
              "girth": [["overgirth", 3], ["girth", 3], ["stud girth", 4], ["stud guard", 4]],
              "glove": [["glove", 3], ["carbon pro", 3], ["mac wet", 3], ["franlkin pro classic", 3], ["pro tech", 3], ["speed polo", 3], ["all weather", 3]],
              "bridle": [["brow band", 3], ["browband", 3], ["caverson", 3], ["headpiece", 3], ["cheekpiece", 3], ["cheek piece", 3], ["curb chain", 5], ["nose band", 3], ["martingale", 3], ["rein", 3], ["noseband", 3], ["bridle", 4], ["breastplate", 3], ["flash", 3]],
              "bit": [["gag", 5], ["loose ring", 3], ["pelham", 5], ["bit", 3], ["bomber", 2], ["happy tongue", 5], ["eggbutt", 3], ["t bar", 3], ["Cosquejero", 5], ["snaffle", 3]],
              "clothes": [["waterproof coat", 3], ["rain coat", 3], ["softshell", 3], ["vest", 3], ["training top", 4], ["hoody", 4], ["blouson", 4], ["knee stocking", 4], ["tweed cap", 4], ["hoodie", 4], ["riding jacket", 4], ["riding jacket", 4], ["t-shirt", 5], ["t shirt", 5], ["bomber jacket", 4], ["bracelet", 5], ["gilet", 5], ["belt", 3], ["alpargata", 5], ["baseball cap", 4], ["cap", 1], ["ear ring", 4], ["earring", 4], ["pendant", 4], ["key ring", 4], ["charm", 4], ["keyring", 4], ["sweater", 3]],
              "whip": [["whip", 3], ["crop", 3], ["jumping bat", 3], ["baton", 4], ["bat ", 2], ["show cane", 3], ["leather cane", 3], ["contact stick", 3], ["touch stick", 3]],
              "helmet": [["helmet", 3], ["wellington professional hat", 5], ["ayrbrush", 4], ["ayr brush", 4], ["skull", 1], ["young rider", 3], ["headband", 2], ["skull hat", 3], ["your instinct", 4], ["face guard", 3], ["Polo Headband", 3], ["faceguard", 3], ["riding hat", 4]],
              "saddle": [["micropile pad", 4], ["saddle", 1], ["bareback riding", 3], ["bates", 3], ["saddle cover", 3], ["Saddle rack", 3], ["saddle soap", 3], ["sticky seat", 3], ["grib stick", 3]],
              "numnah": [["saddle cloth", 3], ["saddlecloth", 3], ["saddle blanket", 3], ["gel saddle pad", 3], ["saddle pad", 3], ["numnah", 4], ["saddlepad", 3], ["saddle cloth", 3]],
              "glasses": [["glasses", 5], ["oculi", 3], ["goggles", 5], ["lens", 5], ["BluEye", 3], ["eyeshield", 3], ["oakley", 3]],
              "glasses_cleaning": [["stericlens", 4], ["nettex", 4], ["net-tex", 4]],
			  "chaps": [["chaps", 3], ["gater", 3], ["gaiter", 3]],
              "headcollar": [["quick clip safety tie", 4], ["headcollar", 4], ["leadrope", 4], ["lead rope", 4], ["head collar", 3]],
              "mallet": [["mallet", 3], ["stick", 1], ["cane", 3], ["Pick Up Stick", 4]],
              "trousers": [["jodphurs", 5], ["jiggy jods", 4], ["jodhpur", 5], ["polo jeans", 3], ["breeches",5], ["whites", 3], ["white jeans", 3], ["wrangler jean", 3], ["passion polo", 3], ["riding tights", 3], ["full seat tights", 3], ["tights", 3], ["tredstep symphony nero", 5], ["darjeen jeans grip", 5], ["all weather pants riding", 5], ["euro-star all weather pants", 5], ["finntack pro all weather", 5]],
              "socks": [["sock", 2]],
              "bandages": [["tail guard", 4], ["tail bag", 5], ["bandage", 3], ["security strap", 3]],
              "spurs": [["spur", 4]],
              "kneepad":[["knee pad", 3], ["kneepad", 3], ["kneeguard", 3], ["Leather Velcro strap", 3]],
              "limb_supports":[["elbow support", 3], ["shoulder protector", 3], ["elbow guard", 3], ["knee support", 3], ["ankle support", 3], ["wrist support", 3], ["wrist wrap", 3], ["wrist compression wrap", 3], ["back support", 3], ["elbow pad", 3]],
              "studs":[["stud", 3]],
              "hoof_oil":[["stockholm hoof tar", 4], ["stockholm tar", 4], ["hoof oil", 3], ["Kevin Bacon", 4], ["Effol", 3]],
              "rug":[["thermatex", 3], ["Summer Sheets", 3], ["weatherbeeta", 3], ["turnout rug", 3], ["00d", 2], ["00g", 2], ["rug", 2], ["shires tempest", 3], ["combo fly rug", 3], ["fly rug", 3], ["combo rug", 3], ["turnout", 3]],
              "show_jacket":[["show jacket", 4]],
              "masks": [["face mask", 4], ["mask", 2], ["face covering", 4]],
              "neck_wear": [["scrunchie", 4], ["stock", 1], ["show tie", 4], ["tie", 1], ["Spur Of The Moment Unisex Silk Tie", 4]],
              "wellington_boots": [["welly boot", 4], ["wellington boot", 4], ["wellington", 3], ["wellies", 3], ["Le Chameau", 4]],
              "grooming_kit": [["grooming box", 3], ["tack box", 3], ["groom", 1], ["brush", 2], ["curry comb", 3], ["grooming kit", 5], ["grooming bag", 5], ["grooming", 2], ["comb", 1]],
              "muzzle": [["muzzle", 3]],
              "body_protector": [["body protector", 4], ["back protector", 4], ["Airowear ayrps", 5]],
              "wheelbarrow": [["wheelbarrow", 3], ["barrow", 3]],
              "haynets": [["haynet", 3], ["hay net", 3], ["hay bag", 5], ["haylage net", 3], ["hay tidy bag", 5], ["haybag", 4]],
              "base_layer": [["base layer", 3], ["base layer", 3], ["baselayer", 3]],
              "polo_shirt": [["polo shirt", 2]],
              "naf": [["naf", 1], ["naf off", 2]],
              "equine_america": [["equine america", 1]],
              "stirrup":[["stirrup", 3], ["flex-on green", 3], ["flex-on safe", 3]],
              "plaiting":[["plaiting", 4], ["plait", 3]],
              "dog": [["chappie", 4], ["wag drying bag", 3], ["towel bag", 3], ["bag dispenser", 3], ["eco bag", 3], ["poop bag", 4], ["beeztees tripe bag", 4], ["romp-n-roll", 4], ["teaser jolly ball", 4], ["treat ball", 3], ["teaser ball", 3], ["puppy", 4], ["kong", 4], ["boot pet bed", 5], ["boot bed", 5], ["dog", 5], ["tennis ball", 3], ["ball", 2], ["chappie favourites mixed selection", 5], ["pure meat stick", 3], ["clix target stick", 4], ["house of paws", 4], ["dental stick", 4]],
              "show_shirt": [["show shirt", 3]],
              "jacket": [["fleece jacket", 3], ["puffer", 3], ["jacket", 1], ["tweed jacket", 3]],
              "herbs": [["herbs", 1]],
              "hat": [["hat", 1]],
              "coat": [["coat", 1]],
              "shampoo": [["lemieux brite whites shampoo", 4], ["shampoo", 2]],
              "underwear": [["boxers", 3], ["booty sleep", 4], ["underwear", 3]],
              "repellent": [["repellent", 1]],
              "garlic": [["garlic", 1]],
              "vitamins": [["vitamin", 2]],
              "cortaflex": [["cortaflex", 5]],
              "scarf": [["neck gaiter", 4], ["scarf", 2]],
              "clippers": [["clipper", 3], ["trimmer", 3]],
              "lick": [["lick", 1], ["likit", 5]],
              "shirts": [["shirt", 1], ["tank top", 3]],
              "conditioner": [["conditioner", 2]],
              "shoes": [["shoe", 1]],
              "lunging": [["lunge", 3]],
              "wraps": [["wrap", 1]],
              "fleece": [["fleece", 1]],
              "twitch": [["twitch", 3]],
              "fly_mask": [["fly veil", 3], ["eye saver", 3]],
              "hoof_dressing": [["hoof dressing", 3], ["hoof klense", 4], ["hoof sticker", 4]],
              "hoof_pick": [["hoof pick", 3]],
              "balancer": [["balancer", 3]],
              "feed": [["youngstock", 4], ["baileys", 4], ["feed", 1], ["hi-fi", 3], ["alfa", 3], ["chaff", 2], ["molasses", 2], ["20kg", 1], ["15kg", 1], ["burgess excel", 3], ["rabbit food", 3]],
              "scoops": [["scoop", 2]],
              "jumping_block": [["jump block", 2], ["pro jump", 1], ["jumping block", 2]],
              "tools": [["socket", 3], ["socket tool", 3], ["polytape", 3], ["tie twister", 4], ["flexible twisty tie", 4], ["tie out stake", 4], ["gate handle", 4], ["fencing post", 4], ["cable tie", 4], ["fence warning sign", 4], ["tie ring", 4], ["tape clamp", 4], ["broom", 3], ["fork", 3], ["tidee", 3]],
              "buckets": [["h2go", 5], ["bucket", 1], ["tubtrug", 4]],
              "manger": [["manger", 3]],
              "mounting block": [["mounting block", 3]],
              "treats": [["leovet", 4], ["horse treat", 4], ["fruities", 4], ["lick mat", 4], ["leoveties", 4], ["treaties", 3], ["treat bag", 4], ["hoarse sweet", 4], ["treats", 2], ["treat bar", 4], ["bizzy bites", 4], ["stud muffin", 4], ["candy cane", 4], ["herb stick", 3], ["carrot stick", 3], ["nibble stick", 3]],
              "toys": [["toy", 1]],
              "bin": [["bin ", 1]],
              "fencing": [["battery", 3]],
              "chalk": [["chalk", 4], ["gold label show", 3]],
              "rabbit": [["rabbit", 4]],
              "handbag": [["handbag", 3], ["cartridgebag", 3], ["tote bag", 3], ["gift bag", 4], ["bottle bag", 3], ["shoulder bag", 3], ["cluth flap", 2], ["grab bag", 2], ["shopper bag", 2], ["tote bag", 3]],
              "dressage_marker": [["stick-on dressage marker", 3], ["stick-on letter", 3]],
			  "gifts": [["pony mad stocking", 4], ["christmas", 5], ["birthday", 5], ["national trust", 4], ["wrendale", 5], ["hi ball", 4], ["tumbler glass", 4], ["brooch", 4], ["stock pin", 4], ["gold plated", 4], ["pony pals party goody bag", 4], ["makasi ducks in boots", 4], ["stick half cube padblocks", 4], ["sticker book", 3], ["classic canes ivory labrador", 4]],
			  "lipbalm": [["lip care stick", 3], ["lip balm", 3], ["lip-balm", 3], ["lipbalm", 3], ["lip-care", 3], ["lip care", 3], ["lip butter", 3]],
			  "cribbing": [["cribstick", 3], ["crib", 2]],
			  "measuring":[["measuring", 3]],
			  "high_vis": [["hi-viz", 4], ["hyviz", 4], ["equi-flector", 4], ["reflective", 4], ["hi viz", 4]],
			  "car":[["boot 'n' bumper", 4], ["boot bed", 4]],
			  "vegan": [["synthetic", 2], [" pu ", 2]],
			  "hayball": [["hayball", 4], ["hay ball", 4]],
			  "cat": [["feline", 5], ["cat", 5], ["catnip", 5]],
			  "bird": [["wolseley peasant", 4], ["cockatiel", 4], ["uncle jimmy hangin' ball", 4], ["loktop", 3], ["fat ball feeder", 3], ["ball feeder", 3]],
			  "misc": [["heat log", 3], ["garden", 3], ["stockboard", 3], ["cafetiere", 4], ["smart garden", 4], ["16 nut", 4], ["freezer bag", 4], ["masking tape", 4], ["oakley summerhouse", 6], ["cropped", 3], ["chinos", 5], ["zubat", 3], ["seed", 4], ["microporous tape", 4], ["loaders bag", 4], ["lumpwood", 4], ["finsbury", 4], ["cross-body bag", 4], ["game bag", 4], ["cartridge", 4], ["messenger", 4], ["clutch", 4], ["tote", 4], ["underarm tweed bag", 4], ["cooling bag", 4], ["camera bag", 4], ["paper bag", 4], ["espadrille bag", 4], ["tip bag", 4], ["summer bag", 4], ["cosmetic bag", 4], ["potato bag", 4], ["animal bag", 4], ["lunch bag", 4], ["make up bag", 4], ["foldaway bag", 4], ["hip flask", 4], ["shopping bag", 4], ["canvas print bag", 4], ["planter bag", 4], ["first aid", 4], ["peg bag", 4], ["cabbage", 4], ["rubble sack", 4], ["garden sack", 4], ["growbag", 4], ["sand maxi bag", 4], ["bags on board", 4], ["jute bag", 4], ["wash-bag", 4], ["wash bag", 4]],
			  "supplements": [["supplement", 5], ["liver klense", 4], ["colostrum", 5], ["formula", 5], ["brewers yeast", 5], ["epsom salt", 5], ["turmeric", 5]],
			  "medical": [["eczema", 4], ["louse powder", 4], ["syringe", 4], ["cryochaps", 4], ["therapy", 4], ["equine haler", 4], ["first aid", 4]],
			  "torch": [["torch", 4]],
			  "catering": [["beer glass", 3]],
			  "horse_face": [["ear net", 4], ["zeb-tek", 4], ["zeb tek", 4], ["fly protector defender mask", 4], ["fly hood", 3], ["half mask", 3], ["mesh mask", 4], ["eye shield", 4], ["flymask", 4], ["fly mask", 4], ["evysor", 5]],
			  "transport": [["tether tie", 4], ["anti pull-back", 4], ["anti-pull back", 4], ["pull-back tie", 4], ["coil tie", 4], ["bungee tie", 4], ["tie chain", 4], ["trailer safety tie", 4], ["trailer", 4], ["trailer tie", 3]],
			  "fence": [["stock fencing", 3], ["wire", 3], ["estate wire", 3]],
			  }




brands = [["stierna", 5], ["thermatex", 5], ["leoveties", 5], ["covalliero", 5], ["kruuse", 5], ["pet stuff", 5], ["earlswood", 5], ["red gorilla", 5], ["hillbrush", 5], ["big tidee", 5], ["caldwells", 5], ["km elite", 5], ["wilkinson sword", 5], ["eazitools", 5], ["equine essentials", 5], ["harold moore", 5], ["herbie", 5], ["gorilla riddler", 5], ["future fork", 5], ["evysor", 5], ["wrendale", 5], ["stericlens", 5], ["nettex", 5], ["net-tex", 5], ["husqvarna", 5], ["petrie", 5], ["horsemens pride", 5], ["ice gorilla", 5], ["fairfax & favor", 5], ["icehorse", 5], ["casablanca", 5], ["ona", 1], ["charles owen", 5], ["armis", 5], ["instinct", 4], ["salvavita", 5], ["lascano", 5],
         ["pampeano", 5], ["ainsley", 5], ["ssg", 5], ["professionals choice", 2], ["krono", 5], ["sabona", 5],
         ["berkeley", 5], ["edition", 1], ["tally ho farm", 5], ["oakley", 5], ["rj polo", 1], ["stephens", 2],
         ["sats polo", 1], ["arma", 2], ["eskadron", 5], ["le mieux", 5], ["sabona", 4], ["kneeland", 3], ["vac", 1],
         ["woof wear", 3], ["franklin", 3], ["hook", 3], ["macwet", 2], ["weatherbeeta", 4], ["rambo", 3], ["mac wet", 3],
         ["lemieux", 6], ["equine america", 3], ["pikeur", 3], ["shires", 3], ["aubrion", 3], ["ariat", 3], ["harry hall", 4],
         ["cavallo", 3], ["pikeur", 5], ["dublin", 3], ["noble balance", 3], ["montar madelyn", 5], ["roeckl", 3], ["dubarry", 4],
         ["mountain horse", 3], ["fairfax & favor", 4], ["tattini", 3], ["veredus", 4], ["aigle", 3], ["neue schule", 3], ["joules", 3],
         ["fyna lite", 3], ["fyna-lite", 3], ["fynalite", 3], ["tubtrug", 4], ["schokemohle", 3], ["kavalkade", 3], ["zandona", 3],
         ["fairfax", 3], ["mark todd", 3], ["prolite", 3], ["kiefer", 3], ["hyshine", 3], ["rhinegold", 3], ["rodney powell", 3],
         ["harry hall", 3], ["horze", 2], ["champion", 1], ["karben", 4], ["gatehouse", 3], ["airowear", 3], ["gatehouse", 3],
         ["racesafe", 2], ["dunlop", 3], ["border wellies", 2], ["hunter", 2], ["barbour", 3], ["rockfish", 2], ["Le Chameau", 3],
         ["lincon", 3], ["roma", 3], ["Equilibrium", 2], ["gorilla", 1], ["hy ",1], ["stubbs", 3], ["hippotonic", 4], ["eper-on", 3],
         ["sprenger", 3], ["stubben", 3], ["korsteel", 3], ["jhl", 2], ["horseware", 3], ["rhinegold", 3], ["tuffa", 2], ["hyland", 2],
         ["saxon", 3], ["elico", 3], ["moretta", 3], ["toggi", 3], ["premier equine", 2], ["tredstep", 3], ["tonics", 2],
         ["holland cooper", 3], ["ps of sweden", 4], ["little knight", 2], ["little rider", 2], ["hyspeed", 3], ["derby house", 2],
         ["hywither", 3], ["john whitaker", 4], ["imperial riding", 3], ["bucas", 3], ["hkm", 1], ["kingsland", 3], ["schockemöhle", 4],
         ["christ ", 1], ["ezi-groom", 3], ["eqckusive", 3]]


prodtype = {"bag": [["boot carrier", 4], ["boot bag", 4], ["cooling", 4], ["duffle bag", 4], ["holdall", 4], ["hold all", 4], ["weekend", 4], ["bum bag", 4], ["stable bag", 4], ["garment bag", 4], ["ring bag", 4], ["hat bag", 4], ["helmet bag", 4], ["mallet bag", 4], ["saddle bag", 4], ["kit bag", 4], ["bridle bag", 4], ["stick bag", 4], ["tack bag", 4], ["bandage bag", 4]],
              "horseboot": [["transport air boot", 3], ["eventer", 3], ["smart hind event", 3], ["smart event", 2], ["cavallo simple boot", 4], ["cavallo big foot boot", 4], ["cavallo entry level boot", 3], ["equilibrium tri-zone", 3], ["ultra mesh", 3], ["mesh hybrid", 3], ["mesh lite", 3], ["snug boot pro", 3], ["shoc air xc", 3], ["shoc xc", 3], ["carbon air xc", 4],  ["carbon xc", 3], ["xc elite", 3],  ["xc carbon", 3], ["boot slim sole", 3], ["joint relief", 3], ["easysoaker", 4], ["travel sure", 4], ["over reach", 3], ["overreach", 3], ["easyboot", 5], ["technik protective boot", 4], ["technik protective support boot", 4], ["medicine boot", 3]],
              "horseboot_accessories": [["boot comfort pad", 4], ["scoot boot", 4], ["boot protection pad", 3], ["hoof pad", 3]],
			  "poloboot": [["toddy zip", 4], ["country boot", 4], ["all weather boot", 4], ["all weather", 3], ["carlow", 3], ["kendal", 3], ["carlton", 3], ["groundbreaker", 3], ["muck boot", 3], ["river boot", 3], ["kennet", 3], ["windermere", 3], ["canyon", 3], ["eskimo", 3], ["burford", 3], ["skyline", 3], ["river grain", 3], ["burford", 3], ["abbey", 3], ["eskdale", 3], ["polo boot", 3], ["kensington", 3], ["vermont", 3], ["chelsea", 3], ["gradmere", 3], ["contour", 2], ["ketley", 3], ["aurora", 3], ["heritage", 2], ["galway", 4], ["belford", 3], ["regina", 3], ["berwick", 3], ["riding boot", 3], ["coniston", 4], ["    ", 3], ["moretta", 3], ["waterproof", 1], ["skyline", 3], ["terrain", 3], ["telluride", 3], ["wexford", 3], ["wythburn", 3], ["bromont", 3], ["pinnacle", 3]],
              "poloboot_accessories": [["boot care kit", 3], ["boot stretcher", 4], ["konig boot cream", 4], ["boot shape holder", 4], ["boot scraper", 4], ["bootshaper", 4], ["boot sock", 4], ["boot shaper", 4], ["interchangeable boot top", 4], ["boot replacement closure", 4], ["qhp exchangeable top", 5], ["strap sleeve", 4], ["led boot safety heel clip", 4], ["boot pull", 3], ["boot jack", 3], ["boot mat", 3], ["boot tassels", 3], ["boot pulls", 3], ["laces", 3], ["tree", 3], ["polish", 3], ["spray", 1], ["boot clip", 3], ["liner", 3], ["boot tab", 4], ["buckle pins", 3], ["replacement cable", 4], ["jack", 2]],
              "ball": [["arena", 3], ["grass", 3], ["snow", 3]],
              "girth": [["sleeve", 4], ["guard", 3], ["extension",3], ["cover", 3], ["stud", 3], ["long", 2], ["short", 2], ["dressage", 4], ["sheepskin", 3], ["overgirth", 3], ["surcingle", 4]],
              "glove": [["shooting glove", 3], ["yard glove", 3], ["technical gloves", 2], ["team roper", 4], ["all weather", 3], ["carbon pro", 4], ["speed", 3], ["pro tech", 4], ["franklin pro classic", 4]],
              "bridle": [["martingale stops", 4], ["brow band", 3], ["breastplate cover", 4], ["nose band", 3], ["reins", 2], ["martingale", 3], ["drop noseband", 3], ["cheek pieces", 3], ["noseband", 2], ["breastplate", 3], ["running reins", 3], ["bridle", 3], ["split reins", 3], ["rein stop", 3], ["curb chain", 3], ["lead rein", 3], ["browband", 3]],
              "bit": [["gag", 1], ["waterford", 4], ["barry gag", 3], ["snaffle", 2], ["balding", 3], ["pelham", 5], ["bomber", 2], ["eggbut", 4], ["d-ring", 4], ["happy tongue", 3], ["t bar", 3], ["bit guard", 3], ["golf label", 3]],
              "clothes": [["waterproof", 3]],
              "whip": [["lunging", 4], ["dressage", 3], ["schooling", 3], ["polo", 3], ["event bat", 3], ["jumping", 3]],
              "helmet": [["shadowmatt", 5], ["ayr8", 8], ["palermo", 4], ["young rider", 4], ["palermo ii", 7], ["instinct", 1], ["skull", 1], ["samshield", 4], ["kep cromo", 4], ["kask star", 3], ["ventair", 3], ["vent-air", 3], ["salavita", 4]],
              "helmet_accessories": [["band", 6], ["helmet lining insert", 5], ["ear warmers", 4], ["replacement liner", 5], ["helmet rack", 5], ["cosy helmet hat", 5], ["helmet deodoriser", 5], ["cleaner", 5], ["removable lining", 5], ["helmet lamp", 5], ["helmet light", 5], ["helmet cover", 5], ["hat cover", 5], ["skull cover", 5], ["helmet rack, 4"], ["head band", 6], ["headband", 6], ["sweatband", 6], ["liner", 6], ["peak", 3], ["face guard", 3], ["faceguard", 3]],
              "saddle": [],
              "saddle_accessories":[["saddle rack", 3], ["cream", 3], ["saddle soap", 3], ["saddle cover", 3], ["conditioning soap", 3], ["leathercare", 3], ["cleaner", 2], ["soap", 2], ["saddle stand", 3], ["number holder", 3], ["sticky seat", 3]],
              "glasses": [["prizm", 4], ["jawbreaker", 4], ["path", 4], ["m2", 4], ["radar", 4]],
              "chaps": [],
              "headcollar": [["lead", 3], ["rawhide", 4], ["headcollar", 3], ["head collar", 3]],
              "mallet": [["foot maallet", 3], ["foot stick", 3], ["foot mallet", 3]],
              "trousers_accessories": [["clip", 4]],
              "trousers": [["hi-rise", 3], ["polo", 4], ["jodhpur", 2], ["underbreeches", 3], ["tights", 2], ["breeches", 3], ["whites", 3], ["jeans", 3]],
              "socks": [],
              "bandages": [["tape", 3], ["tail bandage", 4], ["vet flex", 3], ["orthopaedic", 3], ["sportwrap", 3], ["cohesive", 4], ["body bandage", 3], ["bandage pad", 3], ["liner", 3], ["polo", 4]],
              "spurs": [["spur strap", 3], ["spur protector", 3], ["dressage spur", 4], ["interchangeable", 4], ["star", 4], ["disk", 4], ["plastic",2], ["dummy spur",3], ["ball end", 4], ["prince of wales", 4], ["ball", 4]],
              "grooming_kit": [["mane comb", 2], ["groom comb", 3], ["grooming set", 3], ["solocomb", 3], ["scrubbing", 1], ["heritage", 1], ["Water brush", 3], ["bucket brush", 3], ["body brush", 3], ["detangler", 2], ["pulling comb", 3], ["plastic comb", 2], ["grooming kit", 3], ["grooming bag", 3], ["tack box", 3], ["grooming box", 3], ["curry comb", 3], ["tournament bag", 3], ["grooming block", 3], ["tail brush", 3], ["burcket brush", 3], ["microfibre", 3], ["face brush", 3], ["grooming mitt", 3], ["massage glove", 3], ["massaging glove", 3], ["cleaning glove", 3], ["glove towel", 3], ["glove drying towel", 3], ["glove grooming mitt", 3], ["pet grooming glove", 3], ["vinyl glove", 3], ["hoof brush", 3], ["dandy brush", 3], ["razors", 3], ["Detangler brush", 3], ["sweat scraper", 3]],
              "kneepad": [["kneepad", 1], ["knee pad", 1]],
              "kneepad_accessories":[["velcro strap", 3], ["velcro strap", 3], ["replacement", 3], ["kneepad straps", 3]],
              "limb_supports": [["elbow", 3], ["knee", 3], ["ankle", 3], ["wrist", 3], ["back", 2]],
              "studs":[["tap", 3], ["stud", 1], ["brush", 3], ["stud holes", 3], ["stud spanner", 3]],
              "hoof_oil":[],
              "rug":[["turnout", 3], ["comfitec", 1], ["fly", 4], ["fleece", 4], ["dry rug", 4], ["cooler", 4], ["bug rug", 4], ["rug rack", 5], ["green-tec", 3], ["show rug", 3], ["stable rug", 3], ["lightweight", 3], ["100g", 3], ["50g", 2], ["150g", 3], ["200g", 3], ["220g", 3], ["250g", 3], ["300g", 3], ["350g", 3], ["360g", 3], ["400g", 3], ["450g", 3], ["therapy", 3], ["neck", 3]],
              "tools": [["broom", 2], ["rake", 2], ["tidee", 3], ["fork", 2], ["shovel", 2], ["fork head", 3], ["broom head", 3], ["broom handle", 3], ["manure", 3], ["ragwort", 4], ["weeda fork", 4]],
              "plaiting":[["comb", 4], ["band", 3], ["thread", 2]],
              "ball": [["horse playball", 3], ["snak-a-ball", 4], ["hay", 3], ["wash ball", 3], ["feeder", 3], ["treat ball", 3], ["hangin' ball", 4], ["equine play ball", 4], ["carrot", 3]],
			  "stirrup_accessories": [["flex-on green", 3], ["flex-on safe", 3]],
			  "yardboot": [["winter boot, 3"]],
			  "clothes_winter": [["winter", 3], ["thermal", 2]],
			  "helmet_yard": [["boom microphone", 4], ["forest classic helmet", 4], ["3m peltor x3", 5], ["husqvarna", 5], ["arborist", 5], ["arbortec", 5]],
              "helmet_other": [["welding", 4], ["climbing technology", 5], ["x-arbor helmet", 5]],
              "helmet_custom": [["design your own", 4]],

			  }

gend = [["men", " man", 3], ["men", " men", 3], ["men", " male", 3], ["women", "woman", 3], ["women", "women", 3], ["women", "female", 3], ["women", "ladies", 3], ["women", "lady", 3], ["child", "child", 4], ["child", "kid", 4], ["child", "junior", 4], ["child","baby", 4]]


colour_list = ["aubergine", "tan", "dark green", "arctic print", "red geranium", "red fudge", "beige", "chocolate", "cocoa", "khaki", "cyan", "magenta", "scarlet", "light blue", "olive", "oxblood", "fig", "lagoon", "mustard", "clementine", "tropical", "anthracite", "indigo", "grape", "blossom", "denim", " check", "teal", "wine", "lime", "hi viz", "raspberry", "lilac", "charcoal", " red", "yellow", "pistachio", "berry", "jade", "sky", "leopard", "turquoise", "glitter", "neon", "silver", "burgundy", "coral", "plum", "purple", "mint", "rainbow", "floral", "pink", "ocean", "green", "blue", "navy", "brown", "black", "white", "grey", "rose", "quartz", "orange", "turquiose", "aqua", "camoflauge", "gold"]


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      get product name and category
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

gen = ""
brand = ""
cat = ""
col = ""
ptype = ""


def gettype(product):
    product = product.lower()
    results = []
    global gen
    global brand
    global cat
    global ptype
    global col

    #in here we want to call all other functions to get the product details

    #first we get the brand and add it to results
    brand = getbrand(product)
    #print(brand)
    results.append(brand)

    #second we get the product category
    cat = category(product)
    #print("category = " +cat)
    results.append(cat)

    #third we use the category and product name to find the product type
    if "unknown" in cat:
        ptype = "unknown"
    else:
        try:
            ptype = productname(product, cat)
        except:
            #print("CATEGORY NOT FOUND PROBABLE WEIGHTING IMBALANCE, NAME = " + product + "\n")
            ptype = "unknown"
    results.append(ptype)

    #fourth we find out whether its for men, women or children
    gen = gender(product)
    results.append(gen)

    #fifth we try to find out the colour of the item
    col = colour(product)
    results.append(col)
    result = [brand, cat, ptype, gen, col]

    return result


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This is the specific type of the product (for example charles own young rider helmet or palermo)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def productname(product, cat):
    name = []
    weight = []
    #print("passed 1")
    acc_m = 0

    for i in prodtype[cat]:
        if i[0] in product:
            name.append(i[0])
            weight.append(i[1])

    #print("passed 2")
    try:
        ret1, acc_m = productacc(product, cat)
    except:
        pass
    m = 0
    #print("hi")
    #print(acc_m)

    #print("passed 3")
    #print(len(weight))
    if len(weight) != 0:

        m = max(weight)
        res = [i for i, j in enumerate(weight) if j == m]
        final = []
        #print(m)

        for i in res:
            final.append(name[i])

        ret = ' '.join(final)

        #print("passed 4")
        if m > acc_m:
            return ret
        else:
            #print("passed 5")
            change_cat(cat, "_accessories")
            return ret1
    elif acc_m > m :
        #print("passed 5")
        change_cat(cat, "_accessories")
        return ret1
    else:
        #print("passed 6")
        return "unknown"


def productacc(product, cat):
    #print("product acc called")
    name = []
    weight = []

    try:
        for i in prodtype[(cat + "_accessories")]:
            if i[0] in product:
                name.append(i[0])
                weight.append(i[1])
    except:
        pass
        #print("no accessory list")


    if len(weight) != 0:

        m = max(weight)
        res = [i for i, j in enumerate(weight) if j == m]
        final = []


        for i in res:
            final.append(name[i])

        ret = ' '.join(final)


        #print(ret)
        #print(m)

        return ret, m
    else:
        return "unknown"


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This is the company that makes it eg. casablanca, charles owen etc
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def getbrand(product):
    name = []
    weight = []

    for i in brands:
        if i[0] in product:
            name.append(i[0])
            weight.append(i[1])



    if len(weight) != 0:

        m = max(weight)
        res = [i for i, j in enumerate(weight) if j == m]
        final = []


        for i in res:
            final.append(name[i])

        ret = ' '.join(final)
        return ret
    else:
        return "unknown"



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This is what cateogrory of product it is for example helmet
# you want to iterate through the dictionary items
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def category(product):
    cat = []
    weight = []

    for key in categories:
        for i in categories[key]:
            if i[0] in product:
                cat.append(key)
                weight.append(i[1])

    if len(weight) != 0:
        m = max(weight)
        res = [i for i, j in enumerate(weight) if j == m]
        final = []

        for i in res:
            final.append(cat[i])

        final = list(set(final))
        ret = ' '.join(final)
        return ret
    else:
        return "unknown"



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This is easy, what gender it is meant for
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def gender(product):
    name = []
    weight = []

    for i in gend:
        if i[1] in product:
            name.append(i[0])
            weight.append(i[2])

    if len(weight) != 0:

        m = max(weight)
        res = [i for i, j in enumerate(weight) if j == m]
        final = []


        for i in res:
            final.append(name[i])

        ret = ' '.join(final)
        return ret
    else:
        return "unknown"



#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#This is easy, what colour is the item
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def colour(product):
    colours = ""

    for i in colour_list:
        if i in product:
            colours = colours + i + ", "

    if colours == "":
        colours = "unknown"

    return colours






def change_cat(categ, add):
    #print("change cat called")
    global cat
    cat = categ + add
    #print(cat)
    return




#word = "YOUNG RIDER POLO HELMET LINER KID PINK blue green"
word = "Weatherbeeta Kool Coat in Blue"
#print(word)
result = gettype(word)
#print("brand = " + result[0])
#print("category = " + result[1])
#print("product type = " + result[2])
#print("gender = " + result[3])
#print("colour = " + result[4])
