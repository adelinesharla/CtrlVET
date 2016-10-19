#!/bin/sh

cd ..

python manage.py migrate

python manage.py makemigrations cadastro 

python manage.py makemigrations financeiro

python manage.py migrate

