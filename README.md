# learn-django
Learn Django framework

## Source
From https://www.youtube.com/watch?v=F5mRW0jo-U4

## Steps
- Create app folder
- run ```virtualenv -p python3 .```
- run ```source bin/activate```
- might need to install (admin): ```apt install python3-django```
- create sub-folder ```src```
- access ```src```
- run ```django startproject <name> .```
- might need to install django, run ```pip install django```
- START server: ```python manage.py runserver```
- MIGRATE data: ```python manage.py migrate```

1. add new app
   - run ```python manage.py startproject products```
   - add models
   - run makemigrations and migrate
   - add new model to admin
2. change home page
   - add new app pages ```python manage.py startproject pages```
   - add new app to settings.py
   - add pages > views
   - update urls.py

## Create object in shell
- ```python manage.py shell```
- Query all: ```from products.models import Product``` -> ```Product.objects.all()```
- Create new one: ```Product.objects.create(title='2', description='desc', price='22', summary='sum')```