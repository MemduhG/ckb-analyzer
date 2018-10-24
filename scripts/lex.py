"""Script to produce various forms of lemmas and look them up in input."""

import sys
import re
from translit import translit

yek = "êk"
yek_vocalic = "yek"
ke = "ke"
eke = "eke"
kan = "kan"
ekan = "ekan"
open_iza = "e"
open_iza_voc = "ye"
closed_iza = "y"
ane = "ane"

# fname = "tabsep.txt"
# counts = {}
# with open(fname, "r", encoding="utf-8") as infile:
#     for line in infile:
#         try:
#             count, word = line.strip("\n").split("\t")
#         except ValueError:
#             continue
#         counts[word.strip()] = int(count)
#
# for item in counts.keys():
#     stem = item
#     search = item + kan
#     if search in counts:
#         print(item, counts[item], search, counts[search])

print(translit("ane"))
