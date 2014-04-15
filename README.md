# freebos
Incomplete Python API for the Revolution Freebox.
Very few features at the moment, you can only switch your wifi on and off.


## Install
freebos has been successfully tested with Python 2.7 and Python 3.3. You'll need one of these versions to make it run. Install dependencies through virtualenv for Python3 with the command:

    make

Then use it with:

    ./bin/venv/python wifi [on|off]


## Usage
The only command for the moment is `wifi`, used to switch the wifi on or off.

### wifi

    ./bin/venv/python wifi

shows the current wifi status.

    ./bin/venv/python wifi on

turns the wifi on.

    ./bin/venv/python wifi off

turns the wifi off.

