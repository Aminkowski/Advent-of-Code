# elf didn't pack properly => need to rearrange
# rucksack, 2 compartments, item types separated into comps
# 1 item per comp of different type from the rest (rather than 0)
# input = list of all items in each ruck sack, find errors
# item types identified w/ unique ucase or lcase letters
# characters in a line = all items in a sack, # of items in each comp is =
# looking for repeats in each comp, then want 'prio sum' of errors

list = open("demo3.txt")

