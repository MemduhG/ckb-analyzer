import sys
import re

yek = "ێک"
yek_vocalic = "یەک"
ka = "کە"
aka = "ەکە"
kan = "کان"
akan = "ەکان"
open_iza = "ە"
open_iza_voc = "یە"
closed_iza = "ی"
ana = "انە"

fname = "tabsep.txt"
counts = {}
with open(fname,"r",encoding="utf-8") as infile:
    for line in infile:
        try:
            count,word = line.strip("\n").split("\t")
        except ValueError:
            continue
        counts[word.strip()] = int(count)

for item in counts.keys():
    stem = item
    search = item + kan
    if search in counts:
        print(item,counts[item],search,counts[search])
