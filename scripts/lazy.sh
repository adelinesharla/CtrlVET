#!/bin/sh

cd ..

rm db.sqlite3
rm -rf cadastro/migrations
rm -rf financeiro/migrations
python manage.py migrate
python manage.py makemigrations cadastro 
python manage.py makemigrations financeiro
python manage.py migrate
python manage.py createsuperuser --username admin --email joyce.ambrosio@gmail.com
python manage.py loaddata scripts/json_data/*.json
