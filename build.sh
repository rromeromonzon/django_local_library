set -e 

pip install -r requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

# python3 populate_catalog.py

python3 manage.py collectstatic --noinput

python3 manage.py shell < createsu.py
