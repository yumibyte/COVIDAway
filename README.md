To run:

1. open cmd and cd to root dir
2. pip install -r requirements.txt
3. python manage.py runserver
4. open chrome and go to 127.0.0.1:8000

To read database:

1. open cmd and cd to root dir
2. run python manage.py shell
3. run 'from main.models import Individual'
4. run 'Individual.objects.all()' to list all rows in database
5. run 'Individual.objects.all().delete()' to delete all rows in the database