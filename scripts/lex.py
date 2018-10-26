"""Script to produce various forms of lemmas and look them up in input."""

import sys
import re
from translit import translit

yek_vocalic = "yek"
ke = "ke"
kan = "kan"
open_iza_voc = "ye"
ane = "ane"

def noncap(term):
    return "(?:" + term + ")"

def cons_noun(lexeme):
    o = "|"
    ek = "êk"
    eke = "eke"
    ekan = "ekan"
    open_iza = "e"
    closed_iza = "y"
    poss = ["m","t","y","man","tan","yan"]
    bare = lexeme
    indef = lexeme + ek
    definite = lexeme + eke
    plurdef = lexeme + ekan
    bases = [bare,indef,definite,plurdef]
    forms = list(bases)
    for base in bases:
        for p in poss:
            forms.append(base + p)
        forms.append(base + closed_iza)
    forms.append(bare + open_iza)
    for item in forms:
        print(translit(item))

cons_noun("ziman")
