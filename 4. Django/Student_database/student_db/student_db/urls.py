from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("add/", views.add),
    path("student_list/", views.student_list, name="student_list"),

    path("edit/<int:id>", views.student_edit),
    path("delete/<int:id>", views.student_delete),

    path('login/', views.user_login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.user_logout, name="logout")

]
