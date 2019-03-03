# Disease trends

## Install

These installation instructions were tested on the

    Amazon Linux AMI 2018.03.0 (HVM), SSD Volume Type

image from the AWS cloud.

Choose the directory to which this will be installed:

    INSTALL_DIR=~/disease_trends_webapp

### Dependencies

## Python 3.4

This may work with other Python3.x versions, but I have only tested it with Python 3.4

    sudo yum update
    sudo yum install python34

## Libraries

Libraries are installed in a virtual environment

    pip install virtualenv
    virtualenv -p python34 $INSTALL_DIR/virtualenv

Activate it:

    source $INSTALL_DIR/virtualenv/bin/activate

Install dependencies:

    pip install requests validators Django==2.0.13

### Install

Check out the source code from github like this:

    cd $INSTALL_DIR
    # If you don't have git installed:
    sudo yum install git
    git clone https://github.com/mn1/disease_trends

### Set up your environment

Activate the virtual environment if you haven't already done so:

    source $INSTALL_DIR/virtualenv/bin/activate

Set the PYTHONPATH:

    export PYTHONPATH=$INSTALL_DIR/disease_trends/modules

### Test the application

    python -m unittest discover $INSTALL_DIR/disease_trends/test/
    python $INSTALL_DIR/disease_trends/modules/disease_trends/manage.py test get_input

### Run

Start the server by running:

    python disease_trends/modules/disease_trends/manage.py runserver 0:8000

Navigate your browser to http://127.0.0.1:8000/ to see the web application.

