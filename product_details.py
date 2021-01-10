
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#                      WEIGHTING
#                   0 = LOW WEIGHTING (COMMON NAME)
#                   5 = HIGH WEIGHTING (VERY UNCOMMON)(MUST BE THIS IF NAME IS INCLUDED)
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



categories = {"bag": [["boot bag", 4], ["hat bag", 4], ["helmet bag", 4], ["mallet bag", 4], ["saddle bag", 4], ["bag", 1],
              ["kit bag", 4], ["bridle bag", 4], ["stick bag", 4], ["tack bag", 4], ["bandage bag", 4]],
              "boot": [["tendon boot", 3], ["ballistic", 4], ["over reach", 3], ["tendon", 3], ["Racing Tack replacement straps", 4], ["sport boot", 3], ["skid boot", 3], ["sports boot", 1], ["sports medicine boot", 4], ["bell boot", 4]],
              "poloboot": [["zip", 1], ["riding boot", 3], ["polo boot", 2], ["layer boots", 2]],
              "ball": [["ball", 3]],
              "girth": [["overgirth", 3], ["girth", 3]],
              "glove": [["glove", 3], ["carbon pro", 3], ["mac wet", 3], ["franlkin pro classic", 3], ["pro tech", 3], ["speed polo", 3], ["all weather", 3]],
              "bridle": [["brow band", 3], ["caverson", 3], ["headpiece", 3], ["cheekpiece", 3], ["cheek piece", 3], ["curb chain", 3], ["nose band", 3], ["martingale", 3], ["rein", 3], ["noseband", 3], ["bridle", 3], ["breastplate", 3]],
              "bit": [["gag", 5], ["pelham", 5], ["bit", 5], ["bomber", 2], ["happy tongue", 5], ["eggbutt", 3], ["t bar", 3], ["Cosquejero", 5], ["snaffle", 3]],
              "clothes": [["t-shirt", 5], ["bracelet", 5], ["gilet", 5], ["belt", 3], ["alpargata", 5], ["cap", 1], ["ear ring", 4], ["key ring", 4], ["charm", 4], ["keyring", 4], ["sweater", 3]],
              "whip": [["whip", 3]],
              "helmet": [["helmet", 3], ["young rider", 3], ["headband", 2], ["skull hat", 3], ["your instinct", 4], ["face guard", 3], ["Polo Headband", 3], ["faceguard", 3]],
              "saddle": [["saddle", 3]],
              "glasses": [["glasses", 5], ["oculi", 3], ["goggles", 5], ["lens", 5], ["BluEye", 3], ["eyeshield", 3], ["oakley", 3]],
              "chaps": [["chap", 3]],
              "headcollar": [["headcollar", 4], ["leadrope", 4], ["lead rope", 4], ["head collar", 3]],
              "mallet": [["mallet", 3], ["stick", 3], ["cane", 3]],
              "trousers": [["jodphurs", 5], ["polo jeans", 3], ["breeches",5], ["whites", 3], ["white jeans", 3], ["wrangler jean", 3], ["passion polo", 3]],
              "socks": [["socks", 3]],
              "bandages": [["bandage", 4], ["security strap", 3]],
              "spurs": [["spur", 4]],
              "kneepad":[["knee pad", 3], ["kneepad", 3], ["kneeguard", 3], ["Leather Velcro strap", 3]],
              "limb_supports":[["elbow support", 3], ["elbow guard", 3], ["knee support", 3], ["ankle support", 3], ["wrist support", 3], ["wrist wrap", 3], ["wrist compression wrap", 3], ["back support", 3], ["elbow pad", 3]],
              "studs":[["stud", 3]],
              "hoof_oil":[["hoof oil", 3], ["Kevin Bacon", 3], ["Effol", 3]],
              "rug":[["Summer Sheets", 3], ["weatherbeeta", 3], ["turnout rug", 3]]
              }
              



brands = [["casablanca", 5], ["ona", 5], ["charles owen", 5], ["armis", 5], ["instinct", 4], ["salvavita", 5], ["lascano", 5],
         ["pampeano", 5], ["ainsley", 5], ["ssg", 5], ["professionals choice", 2], ["krono", 5], ["sabona", 5], 
         ["berkeley", 5], ["edition", 1], ["tally ho farm", 5], ["oakley", 5], ["rj polo", 1], ["stephens", 2],
         ["sats polo", 1], ["arma", 2], ["eskadron", 5], ["le mieux", 5], ["sabona", 4], ["kneeland", 3], ["vac", 1],
         ["woof wear", 3], ["franklin", 3], ["hook", 3], ["macwet", 2], ["weatherbeeta", 4], ["rambo", 3], ["mac wet", 3]]


prodtype = {"bag": [],
              "boot": [["tendon boot", 4], ["over reach", 3], ["travel boot", 4], ["skid boot", 3], ["sports boot", 3]],
              "poloboot": [],
              "ball": [["arena", 3], ["grass", 3], ["snow", 3]],
              "girth": [],
              "glove": [["technical gloves", 2], ["team roper", 4], ["all weather", 3], ["carbon pro", 4], ["speed", 3], ["pro tech", 4], ["franklin pro classic", 4]],
              "bridle": [["martingale stops", 4], ["brow band", 3], ["breastplate cover", 4], ["nose band", 3], ["reins", 2], ["martingale", 3], ["drop noseband", 3], ["cheek pieces", 3], ["noseband", 2], ["breastplate", 3], ["running reins", 3], ["bridle", 3], ["split reins", 3]],
              "bit": [["gag", 1], ["pelham", 5], ["bomber", 2], ["happy tongue", 3], ["t bar", 3]],
              "clothes": [],
              "whip": [],
              "helmet": [["palermo", 4], ["young rider", 4], ["palermo ii", 7], ["instinct", 1]],
              "helmet_accessories": [["band", 6], ["head band", 6], ["headband", 6], ["sweatband", 6], ["liner", 6], ["peak", 3], ["face guard", 3], ["faceguard", 3]],
              "saddle": [],
              "saddle_accessories":[["saddle cloths", 3], ["saddlecloth", 3], ["saddle blanket", 3], ["gel saddle pad", 3], ["saddle pad", 3]],
              "glasses": [["prizm", 4], ["jawbreaker", 4], ["path", 4], ["m2", 4], ["radar", 4]],
              "chaps": [],
              "headcollar": [["lead", 3], ["rawhide", 4], ["headcollar", 3]],
              "mallet": [["foot maallet", 3], ["foot stick", 3]],
              "trousers": [],
              "socks": [],
              "bandages": [["tape", 3], ["vet flex", 3]],
              "spurs": [],
              "kneepad": [["kneepad", 1], ["knee pad", 1]],
              "kneepad_accessories":[["velcro strap", 3], ["velcro strap", 3], ["replacement", 3], ["kneepad straps", 3]],
              "limb_supports": [["elbow", 3], ["knee", 3], ["ankle", 3], ["wrist", 3], ["back", 2]],
              "studs":[["tap", 3], ["stud", 1], ["brush", 3], ["stud holes", 3], ["stud spanner", 3]],
              "hoof_oil":[],
              "rug":[]
            }

gend = [["men", " man", 3], ["men", " men", 3], ["men", " male", 3], ["women", "woman", 3], ["women", "women", 3], ["women", "female", 3], ["women", "ladies", 3], ["women", "lady", 3],["child", "child", 4], ["child", "kid", 4], ["child", "junior", 4], ["child","baby", 4]]
         

colour_list = [" red", "yellow", "pink", "green", "blue", "navy", "brown", "black", "white", "grey", "orange", "turquiose", "aqua", "camoflauge", "gold"]


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
            print("CATEGORY NOT FOUND PROBABLE WEIGHTING IMBALANCE")
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
print(word)
result = gettype(word)
print("brand = " + result[0])
print("category = " + result[1])
print("product type = " + result[2])
print("gender = " + result[3])
print("colour = " + result[4])


















    
