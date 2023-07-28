from django.db import models

# always run 'python manage.py makemigrations' then 'python manage.py migrate'
# whenever you make changes to models

# Create your models here.
class Product(models.Model):
    title       = models.CharField(max_length=120) # max_length: required
    description = models.TextField(blank=True, null=True)
    price       = models.DecimalField(decimal_places=2, max_digits=100)
    summary     = models.TextField(blank=True)
    featured    = models.BooleanField(default=False)