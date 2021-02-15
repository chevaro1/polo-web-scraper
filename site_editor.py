import re
# LINK = 7
# IMAGE = 0


def clean_up(site, row):
    try:
        run = globals()[site]
        row = run(row)
    except:
        pass
        #print("no clean up script for this site")

    return row

def add_prefix(prefix, suffix):
    return prefix + suffix

def equus(row):
    prefix = "https://www.equus.co.uk"
    prefix2 = "https:"
    row[7] = add_prefix(prefix, row[7])
    row[0] = add_prefix(prefix2, row[0])
    row[0] = re.sub("_{width}x", "", row[0])
    return row

def oakfield_direct(row):
    prefix = "https://www.oakfield-direct.co.uk/"
    row[7] = add_prefix(prefix, row[7])
    row[0] = add_prefix(prefix, row[0])
    return row

def the_saddlery_shop(row):
    prefix = "https://www.thesaddleryshop.co.uk"
    row[7] = add_prefix(prefix, row[7])
    row[0] = add_prefix(prefix, row[0])
    return row

def saddlesdane(row):
    sep = ","
    img = row[0]
    row[0] = img.split(sep, 1)[0]
    return row

def brendon_saddlery(row):
    prefix = "https://www.brendonsaddlery.co.uk/"
    row[7] = add_prefix(prefix, row[7])
    row[0] = add_prefix(prefix, row[0])
    return row

def old_dairy_saddlery(row):
    prefix = "https://www.olddairysaddlery.co.uk"
    row[7] = add_prefix(prefix, row[7])
    row[0] = add_prefix(prefix, row[0])
    return row

def gilberts_equestrian(row):
    prefix = "https://www.gilbertsequestrianandcountry.co.uk/"
    row[7] = add_prefix(prefix, row[7])
    row[0] = add_prefix(prefix, row[0])
    return row

def millbry_hill(row):
    prefix = "https://www.millbryhill.co.uk"
    row[7] = add_prefix(prefix, row[7])
    row[0] = add_prefix(prefix, row[0])
    return row

def equiport(row):
    prefix = "https://www.equiport.co.uk"
    row[7] = add_prefix(prefix, row[7])
    return row
