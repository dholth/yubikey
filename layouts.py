#!/usr/bin/env python
# Enumerate available xkb layouts for the default keyboard
# It might be useful to loop through keyboard x country x variant,
# but I just ran it for the pc104 keyboard.
# Daniel Holth <dholth@fastmail.fm>

import lxml.etree

repository = "/usr/share/X11/xkb/rules/base.xml"

tree = lxml.etree.parse(file(repository))

layouts = tree.xpath("//layout")

for layout in layouts:
    layoutName = layout.xpath("./configItem/name")[0].text
    print layoutName
    for variant in layout.xpath("./variantList/variant/configItem/name"):
        variantName = variant.text
        print layoutName, variantName
