from re import sub
from decimal import Decimal






def getPrice(price):

    try:
        #print("PRICE IN GET PRICE = " + price)
        price = price.replace("\n", " ")
        price = price.split('£', 1)[1]
        #final = re.search('[0-9.]+', price).group()
        #print("price 1 = " + price)
        price = price.split(" ",1)
        if price[0] == "":
            price = price[1]
        else:
            price = price[0]
        #print("price array =" +  price)
        #print("passed trim " + price)
        value = Decimal(sub(r'[^\d.]', '', price))
        value = round(value,2)

        return value

    except:
        print("attempt failed")
        return ("null")


#vid = getPrice("£35.00 £25.00")
#vid = getPrice("£ 22.50")
#print(vid)
#print("call out of function")
