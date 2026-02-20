from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is my Home page")
    return render(request, "home.html")

def about(request):
    # return HttpResponse("This is my about page")
    return render(request, 'about.html')

def login(request):
    # return HttpResponse("This is my login page")
    return render(request, "login.html")

def register(request):
    # return HttpResponse("This is my register page")
    return render(request, 'register.html')

def service(request):
    # return HttpResponse("This is my service page")
    return render(request, 'service.html')