# Disease trends

## Install

Choose the directory to which this will be installed:

    INSTALL_DIR=~/disease_trends_webapp

### Dependencies

## Python 3.4

This may work with other Python3 version, but I have only tested it with Python 3.4

    sudo yum update
    sudo yum install python34
    sudo yum install git

## Libraries

Libraries are installed in a virtual environment

    pip install virtualenv
    virtualenv -p python3 $INSTALL_DIR/virtualenv

Activate it:

    source $INSTALL_DIR/virtualenv/bin/activate

Install dependencies:

    pip install requests validators Django==2.0.13

### Install

Check out the source code from github like this:

    cd $INSTALL_DIR
    git clone https://github.com/mn1/disease_trends

Change to the new directory:

    cd disease_trends

### Set up your environment

Activate the virtual environment if you haven't already done so:

    source $INSTALL_DIR/virtualenv/bin/activate

Set the PYTHONPATH:

    export PYTHONPATH=$INSTALL_DIR/disease_trends/modules

### Test the application

    python -m unittest discover $INSTALL_DIR/disease_trends/test/

### Run

Start the server by running:

    python modules/disease_trends/manage.py runserver 0:8000

Navigate your browser to http://127.0.0.1:8000/get_input/ to see the web application.

## Terms and conditions

This makes Django start a webserver. It is not recommended for production environments. When something goes wrong, you might see embarassing debug messages revealing the internals of the web application.



