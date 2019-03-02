# Disease trends

## Install

Choose the directory to which this will be installed:

    INSTALL_DIR=~/disease_trends_webapp

### Dependencies

    pip install virtualenv

## Create a virtual environment

    virtualenv -p python3 $INSTALL_DIR/virtualenv
    source $INSTALL_DIR/virtualenv/bin/activate

    pip install requests
    pip install validators
    pip install Django==2.0.13

### Download

Check out the source code from github like this:

    git clone https://github.com/mn1/disease_trends

### Set up your environment

Activate the virtual environment if you haven't already done so:

    source $INSTALL_DIR/virtualenv/bin/activate

Set the PYTHONPATH:

    export PYTHONPATH=$INSTALL_DIR:./modules

### Test the installation

    python -m unittest discover $INSTALL_DIR/test/

## Run

Start the server by running:

    python mysite/manage.py runserver 0:8000

Navigate your browser to http://127.0.0.1:8000 to see the web application..


