#!/usr/bin/env python
import json
alphabet_info = json.load(open("alphabetinfo.json", "r"))
working_layouts = set()
for l in alphabet_info['alphabets'].values():
    working_layouts.update(l)
unsupported = set()
for l in alphabet_info['incompatible']:
    unsupported.add(l[0])
print """<html>
<head>
<title>modhex.js supported keyboard layouts</title>
</head>
<body>"""
print "Tried %d layouts<br/>" % (len(working_layouts) + len(unsupported))
print "Support %d layouts<br/>" % len(working_layouts)
print "Unsupported:<br />\n<ul>"
for layout in unsupported:
    print "<li>%s</li>" % layout
print "</ul>"
print "Supported:<br />\n<ul>"
for layout in working_layouts:
    print "<li>%s</li>" % layout
print """</ul>
</body>
</html>"""
