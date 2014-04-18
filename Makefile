PACKAGES = redis requests celery
DEV_PACKAGES = nose ipdb

all: py3

py2:
	[ -e venv/bin/pip ] || virtualenv venv
	./venv/bin/pip install $(DEV_PACKAGES) $(PACKAGES)
	./venv/bin/pip install $(DEV_PACKAGES)

py3:
	[ -e venv/bin/pip ] || pyvenv venv
	./venv/bin/pip install $(DEV_PACKAGES) $(PACKAGES)

test:
	./venv/bin/nosetests --nocapture test.py
