all: modhex.js layouts.html

clean:
	rm -f k2u.py layouts.txt alphabetinfo.json alphabets.txt modhexmap.js

k2u.py: keysyms.txt buildk2u.py
	./buildk2u.py

layouts.txt: layouts.py
	./layouts.py > layouts.txt

alphabetinfo.json: layouts.txt k2u.py buildalphabetinfo.py
	./buildalphabetinfo.py > alphabetinfo.json

alphabets.txt: alphabetinfo.json alphabets.py
	./alphabets.py

modhexmap.js: alphabets.txt stats.py
	./stats.py -n

modhex.js: modhexmap.js modhex.js.in buildmodhexjs.py
	./buildmodhexjs.py

layouts.html: alphabetinfo.json
	./unsupported.py > layouts.html
