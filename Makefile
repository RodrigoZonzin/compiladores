anle: 
	python3 analisadorLexico.py oi.p

ansi: 	
	python3 analisadorSintatico.py 

anse: 

push: 
	git add .
	git commit -m "comitei em $(shell date +%d-%m-%Y)" 
	git push
