web: gunicorn service-flask:app

release: python manage.py db init
release: python manage.py db migrate
release: python manage.py db upgrade