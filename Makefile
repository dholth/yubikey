all: alphabets.txt

clean:
	rm k2u.py layouts.txt alphabetinfo.json alphabets.txt

k2u.py: keysyms.txt buildk2u.py
	./buildk2u.py

layouts.txt: layouts.py
	./layouts.py > layouts.txt

alphabetinfo.json: layouts.txt k2u.py buildalphabetinfo.py
	./buildalphabetinfo.py > alphabetinfo.json

alphabets.txt: alphabetinfo.json alphabets.py
	./alphabets.py
