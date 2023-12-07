install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py


format:	
	black main.py 

test:
	python3 -m pytest -vv test_*.py
	
		
all: install lint format test 