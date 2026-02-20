from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    data = {
        "student": "vishal"
    }
    return render(request, "home.html", data)