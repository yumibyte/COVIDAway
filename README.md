To run:

1. open cmd and cd to root dir
2. Type these commands:
```
pip install -r requirements.txt
python manage.py runserver
```
3. open chrome and go to 127.0.0.1:8000

To read database:

1. open cmd and cd to root dir

2. Type these commands:
```
run python manage.py shell
run 'from main.models import Individual'
run 'Individual.objects.all()' to list all rows in database
run 'Individual.objects.all().delete()' to delete all rows in the database
```
