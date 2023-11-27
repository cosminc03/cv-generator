init-python:
	pyenv install 3.11.6
	pyenv local

init-virtualenv:
	pipenv install --dev

shell:
	pipenv shell

run:
	python app.py

clean:
	pipenv --rm --clear
