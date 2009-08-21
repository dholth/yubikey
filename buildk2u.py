#!/usr/bin/env python
# Build keysym to unicode dictionary from local copy of
# http://www.cl.cam.ac.uk/~mgk25/ucs/keysyms.txt
#
# Daniel Holth <dholth@fastmail.fm>, 2009

k2u = {}
import pprint
for line in file("./keysyms.txt", "r"):
    if not line.startswith("#"):
        splits = line.split()
        if len(splits) >= 2:
            keysym, unichar = line.split()[:2]
            ks = int(keysym, 16)
            k2u[int(keysym, 16)] = unichr(int(unichar[1:], 16))

out = file("k2u.py", "w")
out.write("map = " + pprint.pformat(k2u) + "\n")
