#!/usr/bin/env python
# Put newly-discovered keymaps into modhex.py
# Daniel Holth <dholth@fastmail.fm>, 2009
import string
file("modhex.py", "w").write(
        string.Template(file("modhex.py.in").read()
            ).substitute(dict(ALPHABETS=file("alphabets.txt").read().strip())))
