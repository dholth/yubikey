#!/usr/bin/env python
# Put newly-discovered keymaps into modhex.js
# Daniel Holth <dholth@fastmail.fm>, 2009
import string
file("modhex.js", "w").write(string.Template(file("modhex.js.in").read()).substitute(dict(KEYMAPS=file("modhexmap.js").read())))
