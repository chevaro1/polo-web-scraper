
# LINK = 7
# IMAGE = 0


def clean_up(site, row):
    try:
        run = globals()[site]
        row = run(row)
    except:
        print("no clean up script for this site")

    return row

def add_prefix(prefix, suffix):
    return prefix + suffix


def oakfield_direct(row):
    prefix = "https://www.oakfield-direct.co.uk/"
    row[7] = add_prefix(prefix, row[7])
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
