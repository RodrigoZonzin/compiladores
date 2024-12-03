push: 
	git add .
	git commit -m "comitei em $(shell date +%d-%m-%Y)" 
	git push
