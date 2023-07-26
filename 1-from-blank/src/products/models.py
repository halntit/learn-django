from django.db import models

# always run 'python manage.py makemigrations' then 'python manage.py migrate'
# whenever you make changes to models

# Create your models here.
class Product(models.Model):
    title       = models.TextField()
    description = models.TextField()
    price       = models.TextField()
    summary     = models.TextField(default='')