from django.db import models

# Create your models here.

# Creating class and objects
class Destination(models.Model):  # For connectivity with DB

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
