from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    data = {
        "student": ["Ravi", "Anita", "Karan", "Sneha", "Neha"]
    }
    return render(request, "home.html", data)