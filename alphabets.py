#!/usr/bin/env python
# Write compatible keymaps to alphabets.txt as utf-8 lines.
# Daniel Holth <dholth@fastmail.fm>, 2009

import sys
import json

alphabet_info = json.load(open("alphabetinfo.json", "r"))
alphabets = open("alphabets.txt", "w")

for key in sorted(alphabet_info['alphabets'].keys()):
    alphabets.write(key.encode("utf-8") + "\n")

