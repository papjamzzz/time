setup:
	python3 -m venv venv && venv/bin/pip install -r requirements.txt

run:
	venv/bin/python app.py

push:
	git add -A && git commit -m "$(m)" && git push

.PHONY: setup run push
