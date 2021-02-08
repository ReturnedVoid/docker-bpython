SYS_PYTHON = /usr/bin/python3


build:
	docker build --tag="litteratum/bpython" --force-rm .

install:
	$(SYS_PYTHON) setup.py install --user

clean:
	rm -rf build dist *.egg-info
