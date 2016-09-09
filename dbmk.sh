#!/bin/sh

python manage.py makemigrations

python manage.py migrate

python manage.py makemigrations cadastro 

python manage.py migrate cadastro

python manage.py makemigrations financeiro

python manage.py migrate financeiro

python manage.py migrate

