#!/bin/sh

python manage.py makemigrations && python manage.py migrate && python manage.py createsuperuser --username admin --email joyce.ambrosio@gmail.com