cd ..

del db.sqlite3
del /s /q cadastro\migrations\*.*
rd /s /q cadastro\migrations\
del /s /q financeiro\migrations\*.*
rd /s /q financeiro\migrations\

python manage.py migrate
python manage.py makemigrations cadastro 
python manage.py makemigrations financeiro
python manage.py migrate

python manage.py createsuperuser --username admin --email joyce.ambrosio@gmail.com

python manage.py loaddata scripts\json_data\clientes.json
python manage.py loaddata scripts\json_data\animais.json
python manage.py loaddata scripts\json_data\funcionarios.json
python manage.py loaddata scripts\json_data\laboratorios.json
python manage.py loaddata scripts\json_data\itens.json
python manage.py loaddata scripts\json_data\anos.json