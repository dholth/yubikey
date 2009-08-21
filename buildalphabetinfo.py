#!/usr/bin/env python
# setxkbmap for each gathered layout and look up the yubikey alphabet
# for that layout
#
# Daniel Holth <dholth@fastmail.fm>, 2009

import os
import json
import sys

import keycode

# Set this to a layout you can type in:
RESTORE_LAYOUT = "us"

alphabets = {}
incompatible = []

try:
    for layout in file("layouts.txt"):
        layout = layout.strip()
        rc = os.system("setxkbmap %s" % layout)
        if rc == 0:
            alphabet = keycode.keycodesToKeysyms(layout)
            if alphabet is None or "\x00" in alphabet or len(alphabet) != 16:
                incompatible.append((layout, alphabet))
                continue
            layouts_for_alphabet = alphabets.get(alphabet, [])
            layouts_for_alphabet.append(layout)
            alphabets[alphabet] = layouts_for_alphabet
        else:
            incompatible.append(layout)
    json.dump({'alphabets':alphabets, 'incompatible':incompatible}, sys.stdout, indent=0)
finally:
    os.system("setxkbmap %s" % RESTORE_LAYOUT)

