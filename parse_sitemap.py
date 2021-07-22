
# Python program to convert text
# file to JSON

import os
import json


# the file to be converted to
# json format
here = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(here, 'dragonfly_saddlery.txt')
#filename = 'horze.txt'

# dictionary where the lines from
# text will be stored

res = []
# creating dictionary
with open(filename) as fh:

    for line in fh:
        dict1 = {}
        # reads each line and trims of extra the spaces
        # and gives only the valid words
        #command, description = line.strip().split(None, 1)
        print(line)
        dict1["link"] = line[:-1]
        res.append(dict1)

# creating json file
# the JSON file is named as test1

#with open('result1.json', 'w', encoding='utf-8') as f:
#    json.dump(res, f, ensure_ascii=False, indent=4)

out_file = open("dragonfly_saddlery.json", "w")
json.dump(res, out_file, indent = 4, sort_keys = False)
out_file.close()
