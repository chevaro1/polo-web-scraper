
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      WEIGHTING
#                   0 = LOW WEIGHTING (COMMON NAME)
#                   5 = HIGH WEIGHTING (VERY UNCOMMON)(MUST BE THIS IF NAME IS INCLUDED)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



categories = {"bag": [["boot bag", 4], ["hat bag", 4], ["helmet bag", 4], ["mallet bag", 4], ["saddle bag", 4], ["bag", 1], ["luggage", 4],
              ["kit bag", 4], ["bridle bag", 4], ["stick bag", 4], ["tack bag", 4], ["bandage bag", 4]],
              "boot": [["tendon boot", 3], ["support boot", 3], ["ice boot", 3], ["magnetic boot", 3], ["therapeutic support boot", 3], ["aero magneto", 3], ["ice vibe", 4], ["ice-vibe", 4], ["magnetik", 3], ["hock boot", 3], ["dressage boot", 4], ["splint boot", 3], ["hoof boot", 3], ["front boot", 3], ["reach boot", 3], ["horse boot", 3], ["travel boot", 3], ["travelling boot", 3], ["hing boot", 3], ["poultice boot", 3], ["ballistic", 4], ["over reach", 3], ["tendon", 3], ["Racing Tack replacement straps", 4], ["sport boot", 3], ["freeze boot", 3], ["therapy boot", 3], ["magno boot", 3], ["veredus", 3], ["kentucky horsewear", 4], ["christ boot", 3], ["stable boot", 3], ["skid boot", 3], ["sports boot", 2], ["sports medicine boot", 4], ["bell boot", 4], ["fetlock boot", 3], ["jump boot", 3], ["brushing boot", 3], ["overreach boot", 3], ["fetlock ring", 2]],
              "poloboot": [["riding boot", 3], ["ariat barn", 4], ["country boots", 3], ["twin gore", 3], ["polo boot", 2], ["layer boots", 2], ["boot", 1], ["jodhpur boot", 4]],
              "ball": [["jolly ball", 3], ["horse playball", 3], ["kong", 3], ["snak-a-ball", 4], ["hay ball", 3], ["hayball", 3], ["wash ball", 3], ["feeder ball", 3], ["ball feeder", 3], ["treat ball", 3], ["hangin' ball", 4], ["equine play ball", 4], ["carrot ball", 3]],
              "polo_ball": [["polo ball", 3], ["umpire ball bag", 4], ["ball bag", 3]],
              "girth": [["overgirth", 3], ["girth", 3], ["stud girth", 4], ["stud guard", 4]],
              "glove": [["glove", 3], ["carbon pro", 3], ["mac wet", 3], ["franlkin pro classic", 3], ["pro tech", 3], ["speed polo", 3], ["all weather", 3]],
              "bridle": [["brow band", 3], ["browband", 3], ["caverson", 3], ["headpiece", 3], ["cheekpiece", 3], ["cheek piece", 3], ["curb chain", 5], ["nose band", 3], ["martingale", 3], ["rein", 3], ["noseband", 3], ["bridle", 4], ["breastplate", 3], ["flash", 3]],
              "bit": [["gag", 5], ["loose ring", 3], ["pelham", 5], ["bit", 3], ["bomber", 2], ["happy tongue", 5], ["eggbutt", 3], ["t bar", 3], ["Cosquejero", 5], ["snaffle", 3]],
              "clothes": [["t-shirt", 5], ["bomber jacket", 4], ["bracelet", 5], ["gilet", 5], ["belt", 3], ["alpargata", 5], ["baseball cap", 4], ["cap", 1], ["ear ring", 4], ["earring", 4], ["pendant", 4], ["key ring", 4], ["charm", 4], ["keyring", 4], ["sweater", 3]],
              "whip": [["whip", 3], ["crop", 3], ["baton", 4], ["bat ", 2]],
              "helmet": [["helmet", 3], ["ayrbrush", 4], ["ayr brush", 4], ["skull", 1], ["young rider", 3], ["headband", 2], ["skull hat", 3], ["your instinct", 4], ["face guard", 3], ["Polo Headband", 3], ["faceguard", 3], ["riding hat", 4]],
              "saddle": [["saddle", 1], ["bareback riding", 3], ["bates", 3], ["saddle cover", 3], ["Saddle rack", 3], ["saddle soap", 3]],
              "numnah": [["saddle cloth", 3], ["saddlecloth", 3], ["saddle blanket", 3], ["gel saddle pad", 3], ["saddle pad", 3], ["numnah", 4], ["saddlepad", 3], ["saddle cloth", 3]],
              "glasses": [["glasses", 5], ["oculi", 3], ["goggles", 5], ["lens", 5], ["BluEye", 3], ["eyeshield", 3], ["oakley", 3]],
              "chaps": [["chap", 3]],
              "headcollar": [["headcollar", 4], ["leadrope", 4], ["lead rope", 4], ["head collar", 3]],
              "mallet": [["mallet", 3], ["stick", 3], ["cane", 3], ["Pick Up Stick", 4]],
              "trousers": [["jodphurs", 5], ["jiggy jods", 4], ["jodhpur", 5], ["polo jeans", 3], ["breeches",5], ["whites", 3], ["white jeans", 3], ["wrangler jean", 3], ["passion polo", 3], ["riding tights", 3], ["full seat tights", 3], ["tights", 3], ["tredstep symphony nero", 5], ["darjeen jeans grip", 5], ["all weather pants riding", 5], ["finntack pro all weather", 5]],
              "socks": [["socks", 3], ["sock", 2]],
              "bandages": [["bandage", 3], ["security strap", 3]],
              "spurs": [["spur", 4]],
              "kneepad":[["knee pad", 3], ["kneepad", 3], ["kneeguard", 3], ["Leather Velcro strap", 3]],
              "limb_supports":[["elbow support", 3], ["shoulder protector", 3], ["elbow guard", 3], ["knee support", 3], ["ankle support", 3], ["wrist support", 3], ["wrist wrap", 3], ["wrist compression wrap", 3], ["back support", 3], ["elbow pad", 3]],
              "studs":[["stud", 3]],
              "hoof_oil":[["hoof oil", 3], ["Kevin Bacon", 4], ["Effol", 3]],
              "rug":[["Summer Sheets", 3], ["weatherbeeta", 3], ["turnout rug", 3], ["00d", 2], ["00g", 2], ["rug", 2], ["shires tempest", 3], ["combo fly rug", 3], ["fly rug", 3], ["combo rug", 3], ["turnout", 3]],
              "show_jacket":[["show jacket", 4]],
              "masks": [["face mask", 4], ["mask", 2], ["face covering", 4]],
              "neck_wear": [["scrunchie", 4], ["stock", 1], ["show tie", 4], ["tie", 2]],
              "wellington_boots": [["wellington boot", 4], ["wellington", 3], ["wellies", 3]],
              "grooming_kit": [["grooming box", 3], ["tack box", 3], ["groom", 1], ["brush", 2], ["curry comb", 3], ["grooming kit", 5], ["grooming bag", 5], ["grooming", 2], ["comb", 1]],
              "muzzle": [["muzzle", 3]],
              "body_protector": [["body protector", 4]],
              "wheelbarrow": [["wheelbarrow", 3], ["barrow", 3]],
              "haynets": [["haynet", 3], ["hay net", 3], ["hay bag", 5], ["haylage net", 3]],
              "base_layer": [["base layer", 3], ["base layer", 3], ["baselayer", 3]],
              "polo_shirt": [["polo shirt", 2]],
              "naf": [["naf", 1]],
              "equine_america": [["equine america", 1]],
              "stirrup":[["stirrup", 3]],
              "plaiting":[["plaiting", 4], ["plait", 3]],
              "dog": [["dog", 5], ["tennis ball", 3], ["ball", 2]],
              "show_shirt": [["show shirt", 3]],
              "jacket": [["jacket", 1], ["tweed jacket", 3]],
              "herbs": [["herbs", 1]],
              "hat": [["hat", 1]],
              "coat": [["coat", 1]],
              "shampoo": [["shampoo", 2]],
              "underwear": [["underwear", 3]],
              "repellent": [["repellent", 1]],
              "garlic": [["garlic", 1]],
              "vitamins": [["vitamin", 2]],
              "cortaflex": [["cortaflex", 5]],
              "scarf": [["scarf", 2]],
              "clippers": [["clipper", 3], ["trimmer", 3]],
              "lick": [["lick", 1], ["likit", 3]],
              "shirts": [["shirt", 1]],
              "conditioner": [["conditioner", 2]],
              "shoes": [["shoe", 1]],
              "lunging": [["lunge", 3]],
              "wraps": [["wrap", 1]],
              "fleece": [["fleece", 1]],
              "twitch": [["twitch", 3]],
              "fly_mask": [["fly veil", 3], ["eye saver", 3]],
              "hoof_dressing": [["hoof dressing", 3], ["hoof klense", 4]],
              "hoof_pick": [["hoof pick", 3]],
              "balancer": [["balancer", 3]],
              "feed": [["baileys", 4], ["feed", 1], ["hi-fi", 3], ["alfa", 3], ["chaff", 2], ["molasses", 2], ["20kg", 1], ["15kg", 1], ["burgess excel", 3], ["rabbit food", 3]],
              "scoops": [["scoop", 2]],
              "jumping_block": [["jump block", 2], ["pro jump", 1], ["jumping block", 2]],
              "tools": [["broom", 3], ["fork", 3], ["tidee", 3]],
              "buckets": [["bucket", 1], ["tubtrug", 4]],
              "manger": [["manger", 3]],
              "mounting block": [["mounting block", 3]],
              "treats": [["treats", 2], ["treat bar", 4], ["bizzy bites", 4], ["stud muffin", 4]],
              "toys": [["toy", 1]],
              "bin": [["bin ", 1]],
              "fencing": [["battery", 3]],
              "chalk": [["chalk", 4]],
              "rabbit": [["rabbit", 4]],
              "handbag": [["handbag", 3], ["cartridgebag", 3], ["tote bag", 3], ["gift bag", 4], ["bottle bag", 3], ["shoulder bag", 3], ["cluth flap", 2], ["grab bag", 2], ["shopper bag", 2], ["tote bag", 3]]
              }




brands = [["casablanca", 5], ["ona", 1], ["charles owen", 5], ["armis", 5], ["instinct", 4], ["salvavita", 5], ["lascano", 5],
         ["pampeano", 5], ["ainsley", 5], ["ssg", 5], ["professionals choice", 2], ["krono", 5], ["sabona", 5],
         ["berkeley", 5], ["edition", 1], ["tally ho farm", 5], ["oakley", 5], ["rj polo", 1], ["stephens", 2],
         ["sats polo", 1], ["arma", 2], ["eskadron", 5], ["le mieux", 5], ["sabona", 4], ["kneeland", 3], ["vac", 1],
         ["woof wear", 3], ["franklin", 3], ["hook", 3], ["macwet", 2], ["weatherbeeta", 4], ["rambo", 3], ["mac wet", 3],
         ["lemieux", 6], ["equine america", 3], ["pikeur", 3], ["shires", 3], ["aubrion", 3], ["ariat", 3], ["harry hall", 4],
         ["cavallo", 3], ["pikeur", 5], ["dublin", 3], ["noble balance", 3], ["Montar Madelyn", 5], ["roeckl", 3], ["dubarry", 4],
         ["mountain horse", 3], ["fairfax & favor", 4], ["tattini", 3], ["veredus", 4], ["aigle", 3], ["neue schule", 3], ["joules", 3],
         ["fyna lite", 3], ["fyna-lite", 3], ["fynalite", 3], ["tubtrug", 4], ["schokemohle", 3], ["kavalkade", 3], ["zandona", 3],
         ["fairfax", 3], ["mark todd", 3], ["prolite", 3], ["kiefer", 3], ["lincon", 3]]


prodtype = {"bag": [["boot bag", 4], ["cooling", 4], ["tail bag", 4], ["duffle bag", 4], ["holdall", 4], ["hold all", 4], ["weekend", 4], ["bum bag", 4], ["stable bag", 4], ["garment bag", 4], ["ring bag", 4], ["hat bag", 4], ["helmet bag", 4], ["mallet bag", 4], ["saddle bag", 4], ["kit bag", 4], ["bridle bag", 4], ["stick bag", 4], ["tack bag", 4], ["bandage bag", 4]],
              "boot": [["tendon boot", 4], ["over reach", 3], ["travel boot", 4], ["skid boot", 3], ["sports boot", 3], ["bell boot", 3], ["overreach", 3], ["brushing boot", 3], ["fetlock boot", 3], ["medicine boot", 3]],
              "poloboot": [["country boot", 4], ["carlow", 3], ["kendal", 3], ["carlton", 3], ["groundbreaker", 3], ["muck boot", 3], ["river boot", 3], ["kennet", 3], ["windermere", 3], ["canyon", 3], ["eskimo", 3], ["burford", 3], ["skyline", 3], ["river grain", 3], ["burford", 3], ["abbey", 3], ["eskdale", 3], ["polo boot", 3], ["kensington", 3], ["vermont", 3], ["chelsea", 3], ["gradmere", 3], ["contour", 2], ["ketley", 3], ["aurora", 3], ["heritage", 2], ["galway", 4], ["belford", 3], ["regina", 3], ["berwick", 3], ["riding boot", 3], ["coniston", 4], ["paddock boot", 3], ["moretta", 3], ["waterproof", 1], ["skyline", 3], ["terrain", 3], ["telluride", 3], ["wexford", 3], ["wythburn", 3], ["bromont", 3], ["pinnacle", 3]],
              "poloboot_accessories": [["boot jack", 3], ["boot mat", 3], ["boot tassels", 3], ["boot pulls", 3],["laces", 3], ["tree", 3], ["polish", 3], ["spray", 1], ["boot clip", 3], ["liner", 3], ["boot tab", 4], ["buckle pins", 3], ["replacement cable", 4], ["jack", 2]],
              "ball": [["arena", 3], ["grass", 3], ["snow", 3]],
              "girth": [["sleeve", 4], ["guard", 3], ["extension",3], ["cover", 3], ["stud", 3], ["long", 2], ["short", 2], ["dressage", 4], ["sheepskin", 3], ["overgirth", 3], ["surcingle", 4]],
              "glove": [["shooting glove", 3], ["yard glove", 3], ["technical gloves", 2], ["team roper", 4], ["all weather", 3], ["carbon pro", 4], ["speed", 3], ["pro tech", 4], ["franklin pro classic", 4]],
              "bridle": [["martingale stops", 4], ["brow band", 3], ["breastplate cover", 4], ["nose band", 3], ["reins", 2], ["martingale", 3], ["drop noseband", 3], ["cheek pieces", 3], ["noseband", 2], ["breastplate", 3], ["running reins", 3], ["bridle", 3], ["split reins", 3], ["rein stop", 3], ["curb chain", 3], ["lead rein", 3], ["browband", 3]],
              "bit": [["gag", 1], ["waterford", 4], ["barry gag", 3], ["snaffle", 2], ["balding", 3], ["pelham", 5], ["bomber", 2], ["eggbut", 4], ["d-ring", 4], ["happy tongue", 3], ["t bar", 3], ["bit guard", 3], ["golf label", 3]],
              "clothes": [],
              "whip": [["lunging", 4], ["dressage", 3], ["schooling", 3], ["polo", 3], ["event bat", 3], ["jumping", 3]],
              "helmet": [["shadowmatt", 5], ["ayr8", 8], ["palermo", 4], ["young rider", 4], ["palermo ii", 7], ["instinct", 1], ["skull", 1], ["samshield", 4], ["kep cromo", 4], ["kask star", 3], ["ventair", 3], ["vent-air", 3], ["salavita", 4]],
              "helmet_accessories": [["band", 6], ["helmet lining insert", 5], ["ear warmers", 4], ["replacement liner", 5], ["helmet rack", 5], ["cosy helmet hat", 5], ["helmet deodoriser", 5], ["cleaner", 5], ["removable lining", 5], ["helmet lamp", 5], ["helmet light", 5], ["helmet cover", 5], ["hat cover", 5], ["skull cover", 5], ["helmet rack, 4"], ["head band", 6], ["headband", 6], ["sweatband", 6], ["liner", 6], ["peak", 3], ["face guard", 3], ["faceguard", 3]],
              "saddle": [],
              "saddle_accessories":[["saddle rack", 3], ["cream", 3], ["saddle soap", 3], ["saddle cover", 3], ["conditioning soap", 3], ["leathercare", 3], ["cleaner", 2], ["soap", 2], ["saddle stand", 3], ["number holder", 3]],
              "glasses": [["prizm", 4], ["jawbreaker", 4], ["path", 4], ["m2", 4], ["radar", 4]],
              "chaps": [],
              "headcollar": [["lead", 3], ["rawhide", 4], ["headcollar", 3], ["head collar", 3]],
              "mallet": [["foot maallet", 3], ["foot stick", 3]],
              "trousers_accessories": [["clip", 4]],
              "trousers": [["polo", 4], ["jodhpur", 2], ["underbreeches", 3], ["tights", 2], ["breeches", 3], ["whites", 3], ["jeans", 3]],
              "socks": [],
              "bandages": [["tape", 3], ["tail bandage", 4], ["vet flex", 3], ["orthopaedic", 3], ["sportwrap", 3], ["cohesive", 4], ["body bandage", 3], ["bandage pad", 3], ["liner", 3], ["polo", 4]],
              "spurs": [],
              "grooming_kit": [["mane comb", 2], ["grooming kit", 3], ["grooming bag", 3], ["tack box", 3], ["grooming box", 3], ["curry comb", 3], ["tournament bag", 3], ["grooming block", 3], ["tail brush", 3], ["burcket brush", 3], ["microfibre", 3], ["face brush", 3], ["grooming mitt", 3], ["hoof brush", 3], ["dandy brush", 3], ["razors", 3], ["Detangler brush", 3], ["sweat scraper", 3]],
              "kneepad": [["kneepad", 1], ["knee pad", 1]],
              "kneepad_accessories":[["velcro strap", 3], ["velcro strap", 3], ["replacement", 3], ["kneepad straps", 3]],
              "limb_supports": [["elbow", 3], ["knee", 3], ["ankle", 3], ["wrist", 3], ["back", 2]],
              "studs":[["tap", 3], ["stud", 1], ["brush", 3], ["stud holes", 3], ["stud spanner", 3]],
              "hoof_oil":[],
              "rug":[["turnout", 3], ["comfitec", 3], ["rug rack", 5], ["green-tec", 3], ["show rug", 3], ["stable rug", 3], ["lightweight", 3], ["100g", 3], ["50g", 2], ["150g", 3], ["200g", 3], ["220g", 3], ["250g", 3], ["300g", 3], ["350g", 3], ["360g", 3], ["400g", 3], ["450g", 3], ["therapy", 3], ["neck", 3]],
              "tools": [["broom", 2], ["rake", 2], ["tidee", 3], ["fork", 2], ["shovel", 2], ["fork head", 3], ["broom head", 3], ["broom handle", 3], ["manure", 3], ["ragwort", 4], ["weeda fork", 4]],
              "plaiting":[["comb", 4], ["band", 3], ["thread", 2]],
              "ball": [["jolly ball", 3], ["horse playball", 3], ["kong", 3], ["snak-a-ball", 4], ["hay", 3], ["wash ball", 3], ["feeder", 3], ["treat ball", 3], ["hangin' ball", 4], ["equine play ball", 4], ["carrot", 3]]
            }

gend = [["men", " man", 3], ["men", " men", 3], ["men", " male", 3], ["women", "woman", 3], ["women", "women", 3], ["women", "female", 3], ["women", "ladies", 3], ["women", "lady", 3],["child", "child", 4], ["child", "kid", 4], ["child", "junior", 4], ["child","baby", 4]]


colour_list = [" red", "yellow", "pistachio", "berry", "burgundy", "plum", "purple", "mint", "rainbow", "floral", "pink", "ocean", "green", "blue", "navy", "brown", "black", "white", "grey", "rose", "quartz", "orange", "turquiose", "aqua", "camoflauge", "gold"]


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
            print("CATEGORY NOT FOUND PROBABLE WEIGHTING IMBALANCE, NAME = " + product + "\n")
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
#word = "Weatherbeeta Kool Coat in Blue"
#print(word)
#result = gettype(word)
#print("brand = " + result[0])
#print("category = " + result[1])
#print("product type = " + result[2])
#print("gender = " + result[3])
#print("colour = " + result[4])
