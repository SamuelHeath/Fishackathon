#!/bin/bash

pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate

if [ $# -eq 0 ]
    then 
		python3 manage.py runserver localhost:8080
elif [ $# -eq 1 ]
    then 
		python3 manage.py runserver localhost:$1
else 
	python3 manage.py runserver $1:$2
fi
