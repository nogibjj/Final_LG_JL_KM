install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C *.py


format:	
	black *.py 

test:
	python3 -m pytest -vv test/test_*.py
	
		
all: install lint format test 