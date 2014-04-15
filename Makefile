PACKAGES = requests
DEV_PACKAGES = nose ipdb

all: py3

dev: py3 py2

py2:
	[ -e venv2/bin/pip ] || virtualenv venv2
	./venv2/bin/pip install $(DEV_PACKAGES) $(PACKAGES)
	./venv/bin/pip install $(DEV_PACKAGES)

py3:
	[ -e venv/bin/pip ] || pyvenv-3.3 venv && wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py && ./venv/bin/python ez_setup.py && ./venv/bin/easy_install pip && rm -f ez_setup.py setuptools-2.1.tar.gz
	./venv/bin/pip install $(PACKAGES)
