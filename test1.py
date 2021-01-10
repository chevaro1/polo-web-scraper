print("hello world, please work")
#from test2 import hello
from product_details import gettype
from product_details import getbrand
from product_details import product


attempt = "Instinct Polo Helmet Black with Black Strap and Black Grommets "
attempt = attempt.lower()
#result = product(attempt, "helmet")
result = gettype("Grey Charles Owen Young Rider")

print(result)

