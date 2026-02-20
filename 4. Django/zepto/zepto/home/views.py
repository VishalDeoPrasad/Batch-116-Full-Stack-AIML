from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'name' : "Amit"
    }
    return render(request, 'home.html', data)