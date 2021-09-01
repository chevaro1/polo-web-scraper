
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      WEIGHTING
#                   0 = LOW WEIGHTING (COMMON NAME)
#                   5 = HIGH WEIGHTING (VERY UNCOMMON)(MUST BE THIS IF NAME IS INCLUDED)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



categories = {"bag": [["luggage", 4], ["whip bag", 4], ["jacket bag", 4], ["tail wrap with bag", 4], ["jodhpur boot bag", 4], ["wellington boot bag", 5], ["boots bag", 4], ["bootbag", 4], ["riding bootbag", 4], ["boot bag", 4], ["hat bag", 4], ["hat carrying bag", 4], ["helmet bag", 4], ["mallet bag", 4], ["saddle bag", 4], ["bag", 1], ["luggage", 4],
              ["kit bag", 4], ["bridle bag", 5], ["stick bag", 4], ["tack bag", 4], ["bandage bag", 4], ["coat bag", 4], ["storage bag", 4], ["feed bag", 4]],
              "horseboot": [["leg pad", 4], ["circulation hoof sock", 4], ["fetlock sock", 4], ["mud sock", 4], ["hoof sock", 4], ["equi-chaps", 4], ["covalliero soft gaiters", 4], ["scoot boot", 4], ["easyboot", 5], ["mud fever boot", 4], ["hybrid boot", 3], ["compression boot", 3], ["procool", 3], ["luxury protection boot", 4], ["woof ultra boot", 4], ["schooling boot", 4], ["hoof gel boot", 4], ["hydro boot", 3], ["brushing boot", 3], ["fetlock boot", 3], ["travel boot", 4], ["skid boot", 3], ["sports boot", 3], ["bell boot", 3], ["leg boot", 4], ["event boot", 3], ["reflective boot", 3], ["tendon boot", 4], ["stable protection boot", 4], ["relief boot", 4], ["soaking boot", 4], ["air flow boot", 4], ["fetlock vent boot", 4], ["fetlock protection boot", 4], ["fly boot", 4], ["flyboot", 4], ["club boot", 3], ["grafter boot", 3], ["exercise boot", 3], ["knee boot", 3], ["shipping boot", 3], ["cross country boot", 4], ["pastern", 4], ["poultice", 4], ["pastern wrap", 4], ["pastern boot", 4], ["tendon boot", 3], ["magnetic chaps", 4], ["equi-chaps, close contact", 4], ["equi-chaps close contact", 4], ["close contact chaps", 4], ["stable chaps", 3], ["hardy chaps", 3], ["support boot", 3], ["ice boot", 3], ["magnetic boot", 3], ["therapeutic support boot", 3], ["aero magneto", 3], ["ice vibe", 4], ["ice-vibe", 4], ["magnetik", 3], ["hock boot", 3], ["dressage boot", 4], ["splint boot", 3], ["hoof boot", 3], ["front boot", 3], ["reach boot", 3], ["horse boot", 3], ["travel boot", 3], ["travelling boot", 3], ["hing boot", 3], ["poultice boot", 3], ["ballistic", 4], ["over reach", 3], ["tendon", 3], ["Racing Tack replacement straps", 4], ["sport boot", 3], ["freeze boot", 3], ["therapy boot", 3], ["magno boot", 3], ["veredus", 3], ["kentucky horsewear", 4], ["christ boot", 3], ["stable boot", 3], ["skid boot", 3], ["sports boot", 2], ["sports medicine boot", 4], ["bell boot", 4], ["fetlock boot", 3], ["jump boot", 3], ["brushing boot", 3], ["overreach boot", 3], ["fetlock ring", 2]],
              "poloboot": [["twin gore", 3], ["polo boot", 2], ["layer boot", 2], ["boot", 1], ["jodhpur boot", 5]],
              "ridingboot":[["pull jack", 4], ["aspen boot", 4], ["riding boot", 3], ["ariat barn", 4], ["twin gore", 3], ["polo boot", 2], ["layer boots", 2], ["boot", 1], ["jodhpur childrens boot", 4], ["jodhpur boot", 4]],
			  "countryboot":[["country boot", 3]],
			  "dressageboot":[],
			  "yardboot": [["dorset high boot", 4], ["skyline summit", 4], ["skyline summit", 4], ["chainsaw boot", 5], ["telluride", 4], ["terrain zip", 4], ["ariat terrain", 4], ["frostline", 3], ["mudbuster", 4], ["mont blanc winter", 4], ["mont blanc winter", 4], ["hercules lace-up", 4], ["muds", 4], ["safety boot", 4], ["wester boot", 4], ["yardmaster boot", 4], ["yardmaster tall boot", 4], ["frost boot", 5], ["muddies", 5], ["hkm davos", 4], ["muck boot", 4], ["mucker boot", 4], ["rain boot", 4], ["rainboot", 4], ["yardboot", 4], ["yard boot", 4]],
			  "boot_maintenance": [["boot shine", 3], ["boot wax", 3], ["boot miracle", 4], ["boots cleaner", 4]],
			  "leather_care":[["saddle soap", 4], ["leather soap", 4], ["oil soap", 4], ["lether", 4], ["leather oil", 4], ["leather balsam", 4], ["leather balm", 4], ["dressing balm", 4], ["leather dressing", 4], ["leather care", 4], ["quick & easy", 4], ["leathercream", 4], ["leather cream", 4], ["leather foam", 4], ["leather quick", 4]],
			  "footwear":[["fairfax & favor", 4], ["burnham", 3], ["regina suede", 3], ["walking boot", 4], ["ladies langham", 4], ["hiking", 3], ["chelsea boot, 4"], ["slippers, 4"]],
			  "ball": [["jolly ball", 3], ["drip feed treat", 3], ["shires ball feeder", 4], ["horsemens pride jolly ball", 4], ["stable  toy", 4], ["carrot ball", 3], ["horse playball", 3], ["snak-a-ball", 4], ["hay ball", 3], ["hayball", 3], ["wash ball", 3], ["feeder ball", 3], ["ball feeder", 3], ["treat ball", 3], ["hangin' ball", 4], ["equine play ball", 4], ["carrot ball", 3]],
              "polo_ball": [["polo ball", 3], ["umpire ball bag", 4], ["ball bag", 3]],
              "girth": [["overgirth", 3], ["girth", 3], ["stud girth", 4], ["stud guard", 4]],
              "glove": [["glove", 4], ["carbon pro", 3], ["mac wet", 3], ["franlkin pro classic", 3], ["pro tech", 3], ["speed polo", 3], ["all weather", 3]],
              "bridle": [["brow band", 3], ["browband", 3], ["caverson", 3], ["headpiece", 3], ["cheekpiece", 3], ["cheek piece", 3], ["curb chain", 5], ["nose band", 3], ["martingale", 3], ["rein", 3], ["noseband", 3], ["bridle", 3], ["breastplate", 3], ["flash", 3]],
              "bit": [["gag", 5], ["balancer bit", 4], ["loose ring", 3], ["pelham", 5], ["bit", 2], ["happy tongue", 5], ["eggbutt", 3], ["t bar", 3], ["Cosquejero", 5], ["snaffle", 3]],
              "clothes": [["rugby", 4], ["boxer", 4], ["sunstopper", 4], ["poncho", 4], ["competition shirt", 4], ["cap", 4], ["bomber", 3], ["waterproof coat", 3], ["rain coat", 3], ["softshell", 3], ["vest", 3], ["training top", 4], ["hoody", 4], ["blouson", 4], ["knee stocking", 4], ["tweed cap", 4], ["hoodie", 4], ["riding jacket", 4], ["riding jacket", 4], ["t-shirt", 5], ["t shirt", 5], ["bomber jacket", 4], ["bracelet", 5], ["gilet", 5], ["belt", 3], ["alpargata", 5], ["baseball cap", 4], ["cap", 1], ["ear ring", 4], ["earring", 4], ["pendant", 4], ["key ring", 4], ["charm", 4], ["keyring", 4], ["sweater", 3]],
              "whip": [["whip", 3], ["crop", 3], ["jumping bat", 3], ["baton", 4], ["bat ", 2], ["show cane", 3], ["leather cane", 3], ["contact stick", 3], ["touch stick", 3]],
              "helmet": [["helmet", 3], ["wellington professional hat", 5], ["ayrbrush", 4], ["ayr brush", 4], ["skull", 1], ["young rider", 3], ["headband", 2], ["skull hat", 3], ["your instinct", 4], ["face guard", 3], ["Polo Headband", 3], ["faceguard", 3], ["riding hat", 3]],
              "saddle": [["gullet", 4], ["micropile pad", 4], ["saddle", 1], ["bareback riding", 3], ["bates", 3], ["saddle cover", 3], ["Saddle rack", 3], ["saddle soap", 3], ["sticky seat", 3], ["grib stick", 3]],
              "numnah": [["saddle cloth", 3], ["saddlecloth", 3], ["saddle blanket", 3], ["gel saddle pad", 3], ["saddle pad", 3], ["numnah", 4], ["saddlepad", 3], ["saddle cloth", 3]],
              "glasses": [["glasses", 5], ["oculi", 3], ["goggles", 5], ["lens", 5], ["BluEye", 3], ["eyeshield", 3], ["oakley", 3]],
              "glasses_cleaning": [["stericlens", 4], ["nettex", 4], ["net-tex", 4]],
			  "chaps": [["chaps", 3], ["gater", 3], ["gaiter", 3]],
              "headcollar": [["quick clip safety tie", 4], ["headcollar", 4], ["leadrope", 4], ["lead rope", 4], ["head collar", 3]],
              "mallet": [["mallet", 3], ["stick", 1], ["cane", 3], ["Pick Up Stick", 4]],
              "trousers": [["jodphurs", 5], ["jiggy jods", 4], ["jodhpur", 5], ["polo jeans", 3], ["breeches",5], ["whites", 3], ["white jeans", 3], ["wrangler jean", 3], ["passion polo", 3], ["riding tights", 3], ["full seat tights", 3], ["tights", 3], ["tredstep symphony nero", 5], ["darjeen jeans grip", 5], ["all weather pants riding", 5], ["euro-star all weather pants", 5], ["finntack pro all weather", 5]],
              "socks": [["sock", 2]],
              "bandages": [["tail guard", 4], ["fleece bandages", 5], ["sports bandages", 5],  ["tail bag", 5], ["bandage", 3], ["security strap", 3], ["bit wrap", 3], ["bit tape", 3], ["support bandages", 5]],
              "spurs": [["spur", 4]],
              "kneepad":[["knee pad", 3], ["kneepad", 3], ["kneeguard", 3], ["Leather Velcro strap", 3]],
              "limb_supports":[["elbow support", 3], ["shoulder protector", 3], ["elbow guard", 3], ["knee support", 3], ["ankle support", 3], ["wrist support", 3], ["wrist wrap", 3], ["wrist compression wrap", 3], ["back support", 3], ["elbow pad", 3]],
              "studs":[["stud", 3]],
              "hoof_oil":[["hoof balm", 4], ["elastic cream", 4], ["hoof lab", 4], ["hoof hardener", 4], ["frogade", 4], ["hoof lab grease", 4], ["hoof grease", 4], ["stockholm hoof tar", 4], ["stockholm tar", 4], ["hoof oil", 3], ["Kevin Bacon", 4], ["Effol", 3]],
              "rug":[["thermatex", 3], ["Summer Sheets", 3], ["weatherbeeta", 3], ["turnout rug", 3], ["00d", 2], ["00g", 2], ["rug", 2], ["shires tempest", 3], ["combo fly rug", 3], ["fly rug", 3], ["combo rug", 3], ["turnout", 3]],
              "show_jacket":[["show jacket", 4]],
              "masks": [["face mask", 4], ["mask", 2], ["face covering", 4]],
              "neck_wear": [["scrunchie", 4], ["stock", 1], ["show tie", 4], ["tie", 1], ["Spur Of The Moment Unisex Silk Tie", 4]],
              "wellington_boots": [["welly boot", 4], ["wellington boot", 4], ["wellington", 3], ["wellies", 3], ["Le Chameau", 4]],
              "grooming_kit": [["detangler", 3], ["sisal", 3], ["body brush", 3], ["dandy brush", 3], ["flick brush", 3], ["sweat scraper", 3], ["rubber groom", 3], ["grooming mitt", 3], ["tack tray", 3], ["brush", 4], ["comb", 4], ["grooming box", 3], ["groom bag", 4], ["groom ring bag", 4], ["groom accessories bag", 4], ["tack box", 3], ["groom", 1], ["brush", 2], ["curry comb", 3], ["bit curry comb", 4], ["grooming kit", 5], ["grooming bag", 5], ["grooming", 2], ["comb", 1]],
              "muzzle": [["muzzle", 3]],
              "body_protector": [["body protector", 4], ["back protector", 4], ["Airowear ayrps", 5]],
              "wheelbarrow": [["wheelbarrow", 3], ["barrow", 3]],
              "haynets": [["haynet", 3], ["hay net", 3], ["hay bag", 5], ["haylage net", 3], ["hay tidy bag", 5], ["haybag", 4]],
              "base_layer": [["base layer", 3], ["base layer", 3], ["baselayer", 3]],
              "polo_shirt": [["polo shirt", 2]],
              "naf": [["naf", 1], ["naf off", 2]],
              "equine_america": [["equine america", 1]],
              "stirrup":[["stirrup", 3], ["flex-on green", 3], ["flex-on safe", 3]],
              "plaiting":[["braid", 4], ["plaiting", 4], ["plait", 3]],
              "dog": [["pooch", 4], ["herring", 4], ["steak", 4], ["buffalo", 4], ["boar", 4], ["jerky", 4], ["antos dental", 4], ["bakers", 4], ["meaty", 4], ["bunnies", 4], ["turkey", 4], ["puppie", 4], ["canin", 4], ["cheesy", 4], ["diapers", 4], ["bitch", 4], ["pedigree", 4], ["grannicks", 4], ["plaque", 4], ["plaqueoff", 4], ["yakers", 4], ["venison", 4], ["porky", 4], ["sausage", 4], ["beef", 4], ["chicken", 4], ["duck", 4], ["misfits", 4], ["beaphar", 4], ["fish", 4], ["salmon", 4], ["meat", 4], ["chappie", 4], ["wag drying bag", 3], ["towel bag", 3], ["bag dispenser", 3], ["eco bag", 3], ["poop bag", 4], ["beeztees tripe bag", 4], ["romp-n-roll", 4], ["teaser jolly ball", 4], ["treat ball", 3], ["teaser ball", 3], ["puppy", 4], ["kong", 4], ["boot pet bed", 5], ["boot bed", 5], ["dog", 5], ["tennis ball", 3], ["ball", 2], ["chappie favourites mixed selection", 5], ["pure meat stick", 3], ["clix target stick", 4], ["house of paws", 4], ["dental stick", 4]],
              "show_shirt": [["show shirt", 3]],
              "jacket": [["fleece jacket", 3], ["puffer", 3], ["jacket", 1], ["tweed jacket", 3]],
              "herbs": [["herbs", 1], ["hilton herbs", 3]],
              "hat": [["hat", 1]],
              "coat": [["coat", 1]],
              "shampoo": [["no rub", 2], ["silkcare", 4], ["biotin", 4], ["leovet shampoo", 2], ["power shampoo", 4], ["coat sheen", 4], ["body wash", 4], ["lemieux brite whites shampoo", 4], ["shampoo", 2]],
              "underwear": [["boxers", 3], ["booty sleep", 4], ["underwear", 3]],
              "repellent": [["repellent", 1]],
              "garlic": [["garlic", 1], ["garlic granules", 3]],
              "vitamins": [["vitamin", 2]],
              "cortaflex": [["cortaflex", 5]],
              "scarf": [["buff", 4], ["neck gaiter", 4], ["scarf", 3]],
              "clippers": [["clipper", 3], ["trimmer", 3]],
              "lick": [["lick", 1], ["likit", 5]],
              "shirts": [["shirt", 1], ["tank top", 3]],
              "conditioner": [["conditioner", 2]],
              "shoes": [["shoe", 1]],
              "lunging": [["lunge", 3]],
              "wraps": [["wrap", 1], ["bandage pad", 5], ["bandage wrap", 5]],
              "fleece": [["fleece", 1]],
              "twitch": [["twitch", 3]],
              "fly_mask": [["fly veil", 3], ["eye saver", 3]],
              "hoof_dressing": [["hoof dressing", 3], ["hoof klense", 4], ["hoof sticker", 4]],
              "hoof_pick": [["hoof pick", 3]],
              "balancer": [["balancer", 3]],
              "feed": [["stirrer", 2], ["youngstock", 4], ["grass pellets", 3], ["grass nuts", 3], ["baileys", 4], ["feed", 1], ["hi-fi", 3], ["alfa", 3], ["chaff", 2], ["molasses", 2], ["20kg", 1], ["15kg", 1], ["burgess excel", 3], ["rabbit food", 3]],
              "scoops": [["scoop", 2]],
              "jumping_block": [["jump block", 2], ["pro jump", 1], ["jumping block", 2]],
              "tools": [["socket", 3], ["socket tool", 3], ["polytape", 3], ["tie twister", 4], ["flexible twisty tie", 4], ["tie out stake", 4], ["gate handle", 4], ["fencing post", 4], ["cable tie", 4], ["fence warning sign", 4], ["tie ring", 4], ["tape clamp", 4], ["broom", 3], ["fork", 3], ["tidee", 3]],
              "buckets": [["tubtrug", 3], ["tub", 3], ["bucket cover", 3], ["h2go", 5], ["bucket", 1], ["tubtrug", 4]],
              "manger": [["manger", 3]],
              "mounting block": [["mounting block", 3]],
              "treats": [["equi-bites", 4], ["bites", 4], ["gumbits", 4], ["leovet", 2], ["horse treat", 4], ["fruities", 4], ["lick mat", 4], ["leoveties", 4], ["treaties", 3], ["treat bag", 4], ["hoarse sweet", 4], ["treats", 2], ["treat bar", 4], ["bizzy bites", 4], ["stud muffin", 4], ["candy cane", 4], ["herb stick", 3], ["carrot stick", 3]],
              "toys": [["toy", 1]],
              "bin": [["bin ", 1], ["bin liners", 3]],
              "fencing": [["battery", 3]],
              "chalk": [["chalk", 4], ["gold label show", 3]],
              "rabbit": [["rabbit", 4]],
              "handbag": [["handbag", 3], ["cartridgebag", 3], ["tote bag", 3], ["gift bag", 4], ["bottle bag", 3], ["shoulder bag", 3], ["cluth flap", 2], ["grab bag", 2], ["shopper bag", 2], ["tote bag", 4]],
              "dressage_marker": [["stick-on dressage marker", 3], ["stick-on letter", 3]],
			  "gifts": [["slant pad", 4], ["caffe", 4], ["travel mug", 4], ["caddy", 4], ["easter", 4], ["advent", 4], ["bangle", 4], ["necklace", 4], ["coaster", 4], ["pony mad stocking", 4], ["christmas", 5], ["birthday", 5], ["national trust", 4], ["wrendale", 5], ["hi ball", 4], ["tumbler glass", 4], ["brooch", 4], ["stock pin", 4], ["gold plated", 4], ["pony pals party goody bag", 4], ["makasi ducks in boots", 4], ["stick half cube padblocks", 4], ["sticker book", 3], ["classic canes ivory labrador", 4]],
			  "lipbalm": [["lip care stick", 3], ["lip balm", 3], ["lip-balm", 3], ["lipbalm", 3], ["lip-care", 3], ["lip care", 3], ["lip butter", 3]],
			  "cribbing": [["cribstick", 3], ["crib", 2]],
			  "measuring":[["measuring", 3]],
			  "high_vis": [["hi-viz", 4], ["hyviz", 4], ["equi-flector", 4], ["reflective", 4], ["hi viz", 4]],
			  "car":[["boot 'n' bumper", 4], ["boot bed", 4]],
			  "vegan": [["synthetic", 2], [" pu ", 2]],
			  "hayball": [["hayball", 4], ["hay ball", 4]],
			  "cat": [["kitten", 5], ["whiskas", 5], ["felix", 5], ["feline", 5], ["cat", 5], ["catnip", 5]],
			  "bird": [["wolseley peasant", 4], ["cockatiel", 4], ["uncle jimmy hangin' ball", 4], ["loktop", 3], ["fat ball feeder", 3], ["ball feeder", 3]],
			  "misc": [["ferret", 3], ["corrugated", 3], ["0mg", 3], ["950g", 3], ["950g", 3], ["900g", 3], ["850g", 3], ["800g", 3], ["750g", 3], ["700g", 3], ["650g", 3], ["600g", 3], ["550g", 3], ["500g", 3], ["450g", 3], ["oropharma", 4], ["nutribird", 4], ["phytopet", 4], ["terrapin", 4], ["tartar", 4], ["biscuits", 4], ["calci-lux", 4], ["carpet", 4], ["udder", 4], ["obstetrical", 4], ["polyfilla", 5], ["difenacoum", 5], ["pet bowl", 3], ["snail", 3], ["nibble stick", 3], ["cricket", 4], ["blooming", 4], ["pond", 4], ["twistynest", 4], ["cage", 4], ["wild bird", 4], ["gerbil", 4], ["vitakraft", 4], ["piccalilli", 4], ["bird", 4], ["mealworm", 4], ["orlux", 4], ["mouse", 4], ["canary", 4], ["peanut", 4], ["budgerigar", 4], ["dandelion", 4], ["budgie", 4], ["hamster", 4], ["fenugreek", 4], ["niblets", 4], ["carrotys", 4], ["suet", 4], ["plunger", 5], ["mounting bracket", 3], ["goat", 5], ["kombitool", 5], ["brushcutter", 5], ["sealey", 5], ["MP5073", 5], ["sander", 5], ["MP5072", 5], ["bitumen", 4], ["bituminous", 4], ["barrel", 4], ["calf", 4], ["corrosion", 4], ["steel flat bar", 4], ["chisel", 4], ["screwdriver", 4], ["solder", 4], ["popcorn", 4], ["ancol", 4], ["snap", 4], ["drill", 4], ["vetiq", 4], ["guinea pig", 4], ["heat log", 3], ["garden", 3], ["stockboard", 3], ["cafetiere", 4], ["smart garden", 4], ["16 nut", 4], ["freezer bag", 4], ["masking tape", 4], ["oakley summerhouse", 6], ["cropped", 3], ["chinos", 5], ["zubat", 3], ["seed", 4], ["microporous tape", 4], ["loaders bag", 4], ["lumpwood", 4], ["finsbury", 4], ["cross-body bag", 4], ["game bag", 4], ["cartridge", 4], ["messenger", 4], ["clutch", 4], ["tote", 3], ["underarm tweed bag", 4], ["cooling bag", 4], ["camera bag", 4], ["paper bag", 4], ["espadrille bag", 4], ["tip bag", 4], ["summer bag", 4], ["cosmetic bag", 4], ["potato bag", 4], ["animal bag", 4], ["lunch bag", 4], ["make up bag", 4], ["foldaway bag", 4], ["hip flask", 4], ["shopping bag", 4], ["canvas print bag", 4], ["planter bag", 4], ["first aid", 4], ["peg bag", 4], ["cabbage", 4], ["rubble sack", 4], ["garden sack", 4], ["growbag", 4], ["sand maxi bag", 4], ["bags on board", 4], ["jute bag", 4], ["wash-bag", 4], ["wash bag", 4]],
			  "supplements": [["zeolite", 4], ["naf", 4], ["thistle", 4], ["herb", 4], ["lectrosalt", 4], ["nettle", 4], ["entericum", 4], ["supplement", 5], ["seaweed", 3], ["liver klense", 4], ["colostrum", 5], ["formula", 5], ["brewers yeast", 5], ["epsom salt", 5], ["turmeric", 5]],
			  "medical": [["thyforon", 5], ["glycerine", 5], ["gamgee", 5], ["wound", 5], ["dermisol", 5], ["sun guard", 5], ["pig oil", 5], ["itchgon", 4], ["sulphur", 4], ["hydroxide", 4], ["respiratory", 4], ["bio-skin", 4], ["wormer", 4], ["tea-tree", 4], ["hanba-vet", 4], ["propolis", 4], ["medic", 4], ["cold pack", 4], ["tea tree", 4], ["cellsius", 4], ["frogmedic", 4], ["thermo massage", 4], ["thermo-massage", 4], ["ointment", 4], ["teatree", 4], ["salve", 4], ["zinc", 4], ["disinfection", 4], ["bot", 4], ["eczema", 4], ["syringe", 4], ["cryochaps", 4], ["therapy", 4], ["equine haler", 4], ["first aid", 4]],
			  "torch": [["torch", 4]],
			  "catering": [["beer glass", 3]],
			  "horse_face": [["ear net", 4], ["zeb-tek", 4], ["zeb tek", 4], ["fly protector defender mask", 4], ["fly hood", 3], ["half mask", 3], ["mesh mask", 4], ["eye shield", 4], ["flymask", 4], ["fly mask", 4], ["evysor", 5]],
			  "transport": [["tether tie", 4], ["anti pull-back", 4], ["anti-pull back", 4], ["pull-back tie", 4], ["coil tie", 4], ["bungee tie", 4], ["tie chain", 4], ["trailer safety tie", 4], ["trailer", 4], ["trailer tie", 3]],
			  "fence": [["stock fencing", 3], ["wire", 3], ["estate wire", 3]],
			  "show": [["hairnet", 3]],
			  "anti-insect": [["repellent", 4], ["ant", 4], ["flea", 4], ["phaser", 4], ["durativ", 4], ["itch", 4], ["no-bite", 4], ["midge", 4], ["louse powder", 4], ["anti-bite", 4], ["bite", 3]],
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
         ["harry hall", 3], ["horze", 2], ["champion", 1], ["karben", 4], ["airowear", 3], ["gatehouse", 3],
         ["racesafe", 2], ["dunlop", 3], ["border wellies", 2], ["hunter", 2], ["barbour", 3], ["rockfish", 2], ["Le Chameau", 3],
         ["lincon", 3], ["roma", 3], ["Equilibrium", 2], ["gorilla", 1], ["hy ",1], ["stubbs", 3], ["hippotonic", 4], ["eper-on", 3],
         ["sprenger", 3], ["stubben", 3], ["korsteel", 3], ["jhl", 2], ["horseware", 3], ["tuffa", 2], ["hyland", 2],
         ["saxon", 3], ["elico", 3], ["moretta", 3], ["toggi", 3], ["premier equine", 2], ["tredstep", 3], ["tonics", 2],
         ["holland cooper", 3], ["ps of sweden", 4], ["little knight", 2], ["little rider", 2], ["hyspeed", 3], ["derby house", 2],
         ["hywither", 3], ["john whitaker", 4], ["imperial riding", 3], ["bucas", 3], ["hkm", 1], ["kingsland", 3], ["schockemöhle", 4],
         ["christ ", 1], ["ezi-groom", 3], ["eqckusive", 3], ["bridleway", 3], ["hilton herbs", 3], ["horslyx", 4], ["vetwrap", 3],
         ["bitz", 4], ["usg", 2], ["busse", 3]]


prodtype = {"bag": [["boot carrier", "boot carrier", 4], ["boot bag", "boot bag", 4], ["cooling", "cooling", 4], ["duffle bag", "duffle bag", 4], ["holdall", "holdall", 4], ["hold all", "hold all", 4], ["weekend", "weekend", 4], ["bum bag", "bum bag", 4], ["stable bag", "stable bag", 4], ["garment bag", "garment bag", 4], ["ring bag", "ring bag", 4], ["hat bag", "hat bag", 4], ["helmet bag", "helmet bag", 4], ["mallet bag", "mallet bag", 4], ["saddle bag", "saddle bag", 4],
              ["kit bag", "kit bag", 4], ["bridle bag", "bridle bag", 4], ["stick bag", "stick bag", 4], ["tack bag", "tack bag", 4], ["bandage bag", "bandage bag", 4]],
              "horseboot": [["transport air boot", "transport air boot", 3], ["eventer", "eventer", 3], ["smart hind event", "smart hind event", 3], ["smart event", "smart event", 2], ["cavallo simple boot", "cavallo simple boot", 4], ["cavallo big foot boot", "cavallo big foot boot", 4], ["cavallo entry level boot", "cavallo entry level boot", 3], ["equilibrium tri-zone", "equilibrium tri-zone", 3], ["ultra mesh", "ultra mesh", 3], ["mesh hybrid", "mesh hybrid", 3], ["mesh lite", "mesh lite", 3], ["snug boot pro", "snug boot pro", 3], ["shoc air xc", "shoc air xc", 3], ["shoc xc", "shoc xc", 3], ["carbon air xc", "carbon air xc", 4],  ["carbon xc", "carbon xc", 3], ["xc elite", "xc elite", 3],  ["xc carbon", "xc carbon", 3], ["boot slim sole", "boot slim sole", 3], ["joint relief", "joint relief", 3], ["easysoaker", "easysoaker", 4], ["travel sure", "travel sure", 4], ["over reach", "over reach", 3], ["overreach", "overreach", 3], ["easyboot", "easyboot", 5],
              ["technik protective boot", "technik protective boot", 4], ["technik protective support boot", "technik protective support boot", 4], ["medicine boot", "medicine boot", 3]],
              "horseboot_accessories": [["boot comfort pad", "boot comfort pad", 4], ["scoot boot", "scoot boot", 4], ["boot protection pad", "boot protection pad", 3], ["hoof pad", "hoof pad", 3]],
			  "poloboot": [["toddy zip", "toddy zip", 4], ["country boot", "country boot", 4], ["all weather boot", "all weather boot", 4], ["all weather", "all weather", 3], ["carlow", "carlow", 3], ["kendal", "kendal", 3], ["carlton", "carlton", 3], ["groundbreaker", "groundbreaker", 3], ["muck boot", "muck boot", 3], ["river boot", "river boot", 3], ["kennet", "kennet", 3], ["windermere", "windermere", 3], ["canyon", "canyon", 3], ["eskimo", "eskimo", 3], ["burford", "burford", 3],
              ["skyline", "skyline", 3], ["river grain", "river grain", 3], ["burford", "burford", 3], ["abbey", "abbey", 3], ["eskdale", "eskdale", 3], ["polo boot", "polo boot", 3], ["kensington", "kensington", 3], ["vermont", "vermont", 3], ["chelsea", "chelsea", 3], ["gradmere", "gradmere", 3], ["contour", "contour", 2], ["ketley", "ketley", 3], ["aurora", "aurora", 3], ["heritage", "heritage", 2], ["galway", "galway", 4], ["belford", "belford", 3], ["regina", "regina", 3], ["berwick", "berwick", 3], ["riding boot", "riding boot", 3], ["coniston", "coniston", 4], ["moretta", "moretta", 3], ["waterproof", "waterproof", 1], ["skyline", "skyline", 3], ["terrain", "terrain", 3], ["telluride", "telluride", 3], ["wexford", "wexford", 3], ["wythburn", "wythburn", 3], ["bromont", "bromont", 3], ["pinnacle", "pinnacle", 3]],
              "poloboot_accessories": [["boot care kit", "boot care kit", 3], ["boot stretcher", "boot stretcher", 4], ["konig boot cream", "konig boot cream", 4], ["boot shape holder", "boot shape holder", 4], ["boot scraper", "boot scraper", 4], ["bootshaper", "bootshaper", 4], ["boot sock", "boot sock", 4], ["boot shaper", "boot shaper", 4], ["interchangeable boot top", "interchangeable boot top", 4], ["boot replacement closure", "boot replacement closure", 4],
              ["qhp exchangeable top", "qhp exchangeable top", 5], ["strap sleeve", "strap sleeve", 4], ["led boot safety heel clip", "led boot safety heel clip", 4], ["boot pull", "boot pull", 3], ["boot jack", "boot jack", 3], ["boot mat", "boot mat", 3], ["boot tassels", "boot tassels", 3], ["boot pulls", "boot pulls", 3], ["laces", "laces", 3], ["tree", "tree", 3], ["polish", "polish", 3], ["spray", "spray", 1], ["boot clip", "boot clip", 3], ["liner", "liner", 3], ["boot tab", "boot tab", 4], ["buckle pins", "buckle pins", 3], ["replacement cable", "replacement cable", 4], ["jack", "jack", 2]],
              "ball": [["arena", "arena", 3], ["grass", "grass", 3], ["snow", "snow", 3]],
              "girth": [["sleeve", "sleeve", 4], ["guard", "guard", 3], ["extension", "extension", 3], ["cover", "cover", 3], ["stud", "stud", 3], ["long", "long", 2], ["short", "short", 2], ["dressage", "dressage", 4], ["sheepskin", "sheepskin", 3], ["overgirth", "overgirth", 3], ["surcingle", "surcingle", 4]],
              "glove": [["shooting glove", "shooting glove", 3], ["yard glove", "yard glove", 3], ["technical gloves", "technical gloves", 2], ["team roper", "team roper", 4], ["all weather", "all weather", 3], ["carbon pro", "carbon pro", 4], ["speed", "speed", 3], ["pro tech", "pro tech", 4], ["franklin pro classic", "franklin pro classic", 4]],
              "bridle": [["martingale stops", "martingale stops", 4], ["brow band", "brow band", 3], ["breastplate cover", "breastplate cover", 4], ["nose band", "nose band", 3], ["reins", "reins", 2], ["martingale", "martingale", 3], ["drop noseband", "drop noseband", 3], ["cheek pieces", "cheek pieces", 3], ["noseband", "noseband", 2], ["breastplate", "breastplate", 3], ["running reins", "running reins", 3], ["bridle", "bridle", 3], ["split reins", "split reins", 3], ["rein stop", "rein stop", 3], ["curb chain", "curb chain", 3], ["lead rein", "lead rein", 3], ["browband", "browband", 3]],
              "bit": [["gag", "gag", 1], ["waterford", "waterford", 4], ["barry gag", "barry gag", 3], ["snaffle", "snaffle", 2], ["balding", "balding", 3], ["pelham", "pelham", 5], ["bomber", "bomber", 2], ["eggbut", "eggbut", 4], ["d-ring", "d-ring", 4], ["happy tongue", "happy tongue", 3], ["t bar", "t bar", 3], ["bit guard", "bit guard", 3], ["golf label", "golf label", 3], ["weymouth loose ring", "weymouth loose ring", 4]],
              "clothes": [["waterproof", "waterproof", 3]],
              "whip": [["lunging", "lunging", 4], ["dressage", "dressage", 3], ["schooling", "schooling", 3], ["polo", "polo", 3], ["event bat", "event bat", 3], ["jumping", "jumping", 3]],
              "helmet": [["shadowmatt", "shadowmatt", 5], ["ayr8", "ayr8", 8], ["palermo", "palermo", 4], ["young rider", "young rider", 4], ["palermo ii", "palermo ii", 7], ["instinct", "instinct", 1], ["skull", "skull", 1], ["samshield", "samshield", 4], ["kep cromo", "kep cromo", 4], ["kask star", "kask star", 3], ["ventair", "ventair", 3], ["vent-air", "vent-air", 3], ["salavita", "salavita", 4]],
              "helmet_accessories": [["band", "band", 6], ["helmet lining insert", "helmet lining insert", 5], ["ear warmers", "ear warmers", 4], ["replacement liner", "replacement liner", 5], ["helmet rack", "helmet rack", 5], ["cosy helmet hat", "cosy helmet hat", 5], ["helmet deodoriser", "helmet deodoriser", 5], ["cleaner", "cleaner", 5], ["removable lining", "removable lining", 5], ["helmet lamp", "helmet lamp", 5], ["helmet light", "helmet light", 5], ["helmet cover", "helmet cover", 5],
              ["hat cover", "hat cover", 5], ["skull cover""skull cover", 5], ["helmet rack", "helmet rack", 4], ["head band", "head band", 6], ["headband", "headband", 6], ["sweatband", "sweatband", 6], ["liner", "liner", 6], ["peak", "peak", 3], ["face guard", "face guard", 3], ["faceguard", "faceguard", 3]],
              "saddle": [],
              "saddle_accessories":[["saddle rack", "saddle rack", 3], ["cream", "cream", 3], ["saddle soap", "saddle soap", 3], ["saddle cover", "saddle cover", 3], ["conditioning soap", "conditioning soap", 3], ["leathercare", "leathercare", 3], ["cleaner", "cleaner", 2], ["soap", "soap", 2], ["saddle stand", "saddle stand", 3], ["number holder", "number holder", 3], ["sticky seat", "sticky seat", 3]],
              "glasses": [["prizm", "prizm", 4], ["jawbreaker", "jawbreaker", 4], ["path", "path", 4], ["m2", "m2", 4], ["radar", "radar", 4]],
              "chaps": [],
              "headcollar": [["lead rope", "lead", 3], ["rawhide headcollar", "rawhide", 4], ["foal headcollar", "foal", 3], ["leather headcollar", "leather", 3]],
              "mallet": [["foot mallet", "foot maallet", 3], ["foot stick", "foot stick", 3], ["foot mallet", "foot mallet", 3]],
              "trousers_accessories": [["clip", "clip", 4]],
              "trousers": [["hi-rise", "hi-rise", 3], ["polo", "polo", 4], ["jodhpur", "jodhpur", 2], ["underbreeches", "underbreeches", 3], ["tights", "tights", 2], ["breeches", "breeches", 3], ["whites", "whites", 3], ["jeans", "jeans", 3]],
              "socks": [],
              "bandages": [["tape", "tape", 3], ["tail bandage", "tail bandage", 4], ["vet flex", "vet flex", 3], ["orthopaedic", "orthopaedic", 3], ["sportwrap", "sportwrap", 3], ["cohesive", "cohesive", 4], ["body bandage", "body bandage", 3], ["bandage pad", "bandage pad", 3], ["liner", "liner", 3], ["polo", "polo", 4]],
              "spurs": [["spur strap", "spur strap", 3], ["spur protector", "spur protector", 3], ["dressage spur", "dressage spur", 4], ["interchangeable", "interchangeable", 4], ["star", "star", 4], ["disk", "disk", 4], ["plastic", "plastic", 2], ["dummy spur", "dummy spur", 3], ["ball end", "ball end", 4], ["prince of wales", "prince of wales", 4], ["ball", "ball", 4]],
              "grooming_kit": [["mane comb", "mane comb", 2], ["groom comb", "groom comb", 3], ["grooming set", "grooming set", 3], ["solocomb", "solocomb", 3], ["scrubbing", "scrubbing", 1], ["heritage", "heritage", 1], ["Water brush", "Water brush", 3], ["bucket brush", "bucket brush", 3], ["body brush", "body brush", 3], ["detangler", "detangler", 2], ["pulling comb", "pulling comb", 3], ["plastic comb", "plastic comb", 2], ["grooming kit", "grooming kit", 3], ["grooming bag", "grooming bag", 3], ["tack box", "tack box", 3], ["grooming box", "grooming box", 3], ["curry comb", "curry comb", 3], ["tournament bag", "tournament bag", 3], ["grooming block", "grooming block", 3], ["tail brush", "tail brush", 3], ["burcket brush", "burcket brush", 3], ["microfibre", "microfibre", 3], ["face brush", "face brush", 3], ["grooming mitt", "grooming mitt", 3], ["massage glove", "massage glove", 3], ["massaging glove", "massaging glove", 3], ["cleaning glove", "cleaning glove", 3],  ["glove towel", "glove towel", 3], ["glove drying towel", "glove drying towel", 3], ["glove grooming mitt", "glove grooming mitt", 3], ["pet grooming glove", "pet grooming glove", 3], ["vinyl glove", "vinyl glove", 3], ["hoof brush", "hoof brush", 3], ["dandy brush", "dandy brush", 3], ["razors", "razors", 3], ["Detangler brush", "Detangler brush", 3], ["sweat scraper", "sweat scraper", 3]],
              "kneepad": [["kneepad", "kneepad", 1], ["knee pad", "knee pad", 1]],
              "kneepad_accessories":[["velcro strap", "velcro strap", 3], ["velcro strap", "velcro strap", 3], ["replacement", "replacement", 3], ["kneepad straps", "kneepad straps", 3]],
              "limb_supports": [["elbow", "elbow", 3], ["knee", "knee", 3], ["ankle", "ankle", 3], ["wrist", "wrist", 3], ["back", "back", 2]],
              "studs":[["tap", "tap", 3], ["stud", "stud", 1], ["brush", "brush", 3], ["stud holes", "stud holes", 3], ["stud spanner", "stud spanner", 3]],
              "hoof_oil":[],
              "rug":[["turnout", "turnout", 3], ["comfitec", "comfitec", 1], ["fly", "fly", 4], ["fleece", "fleece", 4], ["dry rug", "dry rug", 4], ["cooler", "cooler", 4], ["bug rug", "bug rug", 4], ["rug rack", "rug rack", 5], ["green-tec", "green-tec", 3], ["show rug", "show rug", 3], ["stable rug", "stable rug", 3], ["lightweight", "lightweight", 3], ["100g", "100g", 3], ["50g", "50g", 2], ["150g", "150g", 3], ["200g", "200g", 3], ["220g", "220g", 3], ["250g", "250g", 3], ["300g", "300g", 3],
              ["350g", "350g", 3], ["360g", "360g", 3], ["400g", "400g", 3], ["450g", "450g", 3], ["therapy", "therapy", 3], ["neck", "neck", 3]],
              "tools": [["broom", "broom", 2], ["rake", "rake", 2], ["tidee", "tidee", 3], ["fork", "fork", 2], ["shovel", "shovel", 2], ["fork head", "fork head", 3], ["broom head", "broom head", 3], ["broom handle", "broom handle", 3], ["manure", "manure", 3], ["ragwort", "ragwort", 4], ["weeda fork", "weeda fork", 4]],
              "plaiting":[["comb", "comb", 4], ["band", "band", 3], ["thread", "thread", 2]],
              "ball": [["horse playball", "horse playball", 3], ["snak-a-ball", "snak-a-ball", 4], ["hay", "hay", 3], ["wash ball", "wash ball", 3], ["feeder", "feeder", 3], ["treat ball", "treat ball", 3], ["hangin' ball", "hangin' ball", 4], ["equine play ball", "equine play ball", 4], ["carrot", "carrot", 3]],
			  "stirrup_accessories": [["flex-on green", "flex-on green", 3], ["flex-on safe", "flex-on safe", 3]],
			  "yardboot": [["winter boot", "winter boot", 3]],
			  "clothes_winter": [["winter", "winter", 3], ["thermal", "thermal", 2]],
			  "helmet_yard": [["boom microphone", "boom microphone", 4], ["forest classic helmet", "forest classic helmet", 4], ["3m peltor x3", "3m peltor x3", 5], ["husqvarna", "husqvarna", 5], ["arborist", "arborist", 5], ["arbortec", "arbortec", 5]],
              "helmet_other": [["welding", "welding", 4], ["climbing technology", "climbing technology", 5], ["x-arbor helmet", "x-arbor helmet", 5]],
              "helmet_custom": [["design your own", "design your own", 4]],
              "body_protector": [["Eco Flexi Panel", "eco-flexi", 3], ["Eco Flexi Panel", "eco flexi", 3], ["Airowear wave", "airowear wave", 3], ["Airowear ayrps", "airowear ayrps", 3], ["Racesafe Provent", "provent", 3], ["Airowear outlyne", "outlyne", 3], ["Titanium TI22", "TI22", 4], ["Superflex Sport", "superflex", 3], ["Flexair", "flexair", 3], ["shires Karben", "karben", 4], ["Airowear Flexion", "flexion", 3], ["Airowear Airmesh", "airmesh", 3]]
			  }

gend = [["men", " man", 3], ["men", " men", 3], ["men", " male", 3], ["women", "woman", 3], ["women", "women", 3], ["women", "female", 3], ["women", "ladies", 3], ["women", "lady", 3], ["child", "child", 4], ["child", "kid", 4], ["child", "junior", 4], ["child", "baby", 4]]


colour_list = {
            "White": ["white"],
            "Yellow": ["yellow", "mustard", "leopard"],
            "Orange": ["orange", "clementine"],
            "Red": ["red", "red fudge", "scarlet", "wine", "burgundy", "coral"],
            "Pink": ["pink", "reg geranium", "magenta", "blossom", "raspberry", "berry", "rose", "musk", "heather"],
            "Purple": ["purple", "aubergine", "oxblood", "fig", "grape", "lilac", "plum"],
            "Blue": ["blue", "arctic print", "indigo", "denim", "navy", "ocean"],
            "Light Blue": ["cyan", "light blue", "lagoon", "tropical", "teal", "sky", "turquoise", "aqua", "azure"],
            "Light Green": ["pistachio", "mint"],
            "Green": ["green", "dark green", "olive", "jade", "sage", "peacock"],
            "Brown": ["brown", "chocolate", "cocoa"],
            "Light Brown": ["tan", "beige", "khaki"],
            "Ligh Grey": ["lime", "silver"],
            "Grey": ["grey", "quartz", "slate", "thyme"],
            "Dark Grey": ["dark grey", "anthracite", "charcoal"],
            "Black": ["black"],
            "Hi-viz": ["hi viz", "neon"],
            "Multi Colour": ["rainbow", "floral", "glitter", "camoflauge", "gold", " check", "arctic print"]
}



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
        if i[1] in product:
            name.append(i[0])
            weight.append(i[2])

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
            if i[1] in product:
                name.append(i[0])
                weight.append(i[2])
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
def colourOld(product):
    colours = ""

    for i in colour_list:
        if i in product:
            colours = colours + i + ", "

    if colours == "":
        colours = "unknown"

    return colours

def colour(product):
    colour_string = ""
    colour_array = []

    for key in colour_list:
        for i in colour_list[key]:
            if i in product:
                colour_array.append(key)

    colour_array = list(dict.fromkeys(colour_array))

    for i in colour_array:
        colour_string = colour_string + i + ", "

    return colour_string


def change_cat(categ, add):
    #print("change cat called")
    global cat
    cat = categ + add
    #print(cat)
    return




word = "Weatherbeeta Kool Coat in Blue navy orange turnout"
result = gettype(word)
print("brand = " + result[0])
print("category = " + result[1])
print("product type = " + result[2])
#print("gender = " + result[3])
print("colour = " + result[4])
