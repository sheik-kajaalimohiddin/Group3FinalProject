#!/bin/bash
###Install necessary dependencies###
sudo yum install python -y &> /dev/null
sudo yum install git -y &> /dev/null
sudo yum install pip -y &> /dev/null
sudo pip install virtualenv &> /dev/null
pip install --upgrade pip &> /dev/null
DIR1="eb-virt"
if [ -d "DIR1" ];
then
	source ~/eb-virt/bin/activate
	pip install Django &> /dev/null
	pip install django-crispy-forms &> /dev/null
	python -m pip install Pillow &> /dev/null
	pip install bootstrap &> /dev/null
	pip install psycopg2-binary &> /dev/null
	sudo dnf install -y pip &> /dev/null
	sudo dnf install -y mariadb105-devel gcc python3-devel &> /dev/null
	pip install mysqlclient &> /dev/null
else
	virtualenv ~/eb-virt &> /dev/null
	source ~/eb-virt/bin/activate
	pip install Django &> /dev/null
	pip install django-crispy-forms &> /dev/null
	python -m pip install Pillow &> /dev/null
	pip install bootstrap &> /dev/null
	pip install psycopg2-binary &> /dev/null
	sudo dnf install -y pip &> /dev/null
	sudo dnf install -y mariadb105-devel gcc python3-devel &> /dev/null
	pip install mysqlclient &> /dev/null
fi

DIR=" Group3FinalProject"

if [ -d "$DIR" ];
then
	rm -rf  Group3FinalProject/
	git clone https://github.com/sheik-kajaalimohiddin/Group3FinalProject.git &> /dev/null
	cd  Group3FinalProject/
	python manage.py makemigrations &> /dev/null
	python manage.py migrate &> /dev/null
	python manage.py runserver 0.0.0.0:8000 &> /dev/null
else
	git clone https://github.com/sheik-kajaalimohiddin/Group3FinalProject.git &> /dev/null
	cd  Group3FinalProject/
	python manage.py makemigrations &> /dev/null
	python manage.py migrate &> /dev/null
	python manage.py runserver 0.0.0.0:8000 &> /dev/null
fi
