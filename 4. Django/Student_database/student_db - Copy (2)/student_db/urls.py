from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home, name='home'),
    path("add/", views.add, name='add_student'),
    path("student_list/", views.student_list, name="student_list"),

    path("edit/<int:id>", views.student_edit),

    path("delete/<int:id>", views.student_delete),

    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
