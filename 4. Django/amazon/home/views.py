from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Welcome to Home page:")

def about(request):
    return HttpResponse("Welcome to about page:")

def login(request):
    return HttpResponse("Welcome to Login page:")

def register(request):
    return HttpResponse("Welcome to Register page:")