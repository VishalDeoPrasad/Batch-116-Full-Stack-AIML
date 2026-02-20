from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.home),
    path("about/", views.about),
    path("contact/", views.contact),
    path("login/", views.login),
    path("register/", views.register),
    path("service/", views.service),
]
