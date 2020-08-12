from django.shortcuts import render
from .models import Destination  # Importing from models.py

# Create your views here.


def index(request):

    # Fetching data from the database and adding it to the home page
    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})  # Passing the dests list to index.html