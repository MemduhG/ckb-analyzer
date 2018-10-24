"""
Transliterator from Latin to Sorani letters.
"""

import sys

pairs = [["x", "خ"], ["a", "ا"], ["b", "ب"], ["c", "ج"], ["ç", "چ"],
         ["d", "د"], ["e", "ە"], ["ê", "ێ"], ["f", "ف"], ["H", "ح"],
         ["gh", "غ"], ["g", "گ"], ["h", "ه"], ["i", ""], ["3", "ع"],
         ["î", "ی"], ["j", "ژ"], ["k", "ک"], ["L", "ڵ"], ["l", "ل"],
         ["m", "م"], ["n", "ن"], ["o", "ۆ"], ["p", "پ"], ["q", "ق"],
         ["R", "ڕ"], ["r", "ر"], ["ş", "ش"], ["ş", "ش"], ["s", "س"],
         ["t", "ت"], ["û", "وو"], ["u", "وو"], ["w", "و"], ["v", "ڤ"],
         ["y", "ی"], ["z", "ز"], ["Y", "ئ"]]


def translit(word):
    """Transliterate by replacing characters."""
    out = word.strip()
    if " " in out:
        o = ""
        for item in out.split(" "):
            o += translit(item) + " "
        return o.strip()
    if len(out) == 0:
        return ""
    out.replace("ye", "یە")
    for pair in pairs:
        out = out.replace(pair[0], pair[1])
    return out


if __name__ == "__main__":
    for line in sys.stdin:
        sys.stdout.write(translit(line) + "\n")
