#!/usr/bin/env python
import sys
import pprint

hexa = "0123456789abcdef"

def stats():
    """Build [alphabets, reverseIndex] structure for modhex.js and write to modhexmap.js"""
    numberLetter = {}
    letterNumber = {}

    i = 0
    mappings = []
    alphabets = file("alphabets.txt", "r").readlines()
    alphabets = [x.decode("utf-8").strip() for x in alphabets]
    alphabets.sort()
    for j in alphabets:
        try:
            for n, c in zip(hexa, j):
                numberLetter[n] = numberLetter.get(n, set()).union(set((c,)))
                letterNumber[c] = letterNumber.get(c, set()).union(set((i,)))
            mappings.append(j)
            i+=1
        except Exception, e:
            sys.stderr.write(str(e) + "\n")
            raise

    reverseIndex = {}
    for k in letterNumber:
        reverseIndex[k] = list(letterNumber[k])

    import json
    output = file("modhexmap.js", "w")
    output.write(json.dumps((mappings, reverseIndex), ensure_ascii=False).encode("utf-8"))
    return (numberLetter, letterNumber, mappings)

if __name__ == "__main__":
    numberLetter, letterNumber, mappings = stats()
