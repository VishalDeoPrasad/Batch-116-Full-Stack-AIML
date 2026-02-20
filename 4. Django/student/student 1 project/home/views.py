from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    hours = datetime.now().hour
    min = datetime.now().minute
    sec = datetime.now().second
    data = {
        "hours": hours,
        "minutes": min,
        "second" : sec
    }
    return render(request, "home.html", data)