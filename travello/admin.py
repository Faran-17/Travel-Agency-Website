from django.contrib import admin
from .models import Destination  # importing from models.py

# Register your models here.

admin.site.register(Destination)  # Importing the Destination to the admin page
