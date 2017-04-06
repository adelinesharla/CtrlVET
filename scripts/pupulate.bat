@echo off
cd ..
python manage.py loaddata scripts\json_data\clientes.json
python manage.py loaddata scripts\json_data\animais.json
python manage.py loaddata scripts\json_data\funcionarios.json
python manage.py loaddata scripts\json_data\laboratorios.json


