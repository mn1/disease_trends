
Setup
=====

cd /home/mnuhn/linguamatics

pip install virtualenv

virtualenv /home/mnuhn/linguamatics/virtualenv
source /home/mnuhn/linguamatics/virtualenv/bin/activate

pip install requests
pip install validators
pip install Django
python -m django --version


django-admin startproject mysite

cd mysite/
python manage.py runserver 0:8000

python manage.py startapp polls


python manage.py makemigrations polls

python manage.py migrate


python manage.py createsuperuser

export PYTHONPATH=./modules

python -m unittest discover test/

python mysite/manage.py test polls



# Starting the disease trends app

django-admin startproject modules/disease_trends

python disease_trends/manage.py startapp get_input
python modules/disease_trends/manage.py runserver 0:8000





sudo yum -y install python36u



ssh -i /home/mnuhn/linguamatics/aws_disease_trends.pem ec2-user@35.178.239.253


35.178.239.253:8000


amazon-linux-extras -y install python36u









