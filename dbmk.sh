#!/bin/sh

python manage.py makemigrations

python manage.py migrate

python manage.py makemigrations cadastro 

python manage.py migrate cadastro

python manage.py makemigrations secretaria

python manage.py migrate secretaria

python manage.py migrate

