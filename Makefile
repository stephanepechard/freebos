PACKAGES = requests nose ipdb

all: prod

venv2:
	[ -e venv2/bin/pip ] || virtualenv venv2

venv3:
	[ -e venv3/bin/pip ] || pyvenv-3.3 venv3 && wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py && ./venv3/bin/python ez_setup.py && ./venv3/bin/easy_install pip && rm -f ez_setup.py setuptools-2.1.tar.gz

install:
	./venv2/bin/pip install $(PACKAGES)
	./venv3/bin/pip install $(PACKAGES)

dev: venv2 venv3 install

prod: venv3 install
