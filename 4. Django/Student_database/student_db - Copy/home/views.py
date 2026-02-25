from django.shortcuts import render, redirect
from home.models import Student
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request, "home.html")

@login_required(login_url='login')
def add(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        # print(name, age, mobile, email)
        Student.objects.create(
            name = name,
            age = age,
            mobile = mobile,
            email = email
        )
    return render(request, "add.html")

@login_required(login_url='login')
def student_list(request):
    students = Student.objects.all()
    # print(students)
    data = {
        "students":students
    }

    return render(request, "student_list.html", data)

def student_edit(request, id):
    student = Student.objects.get(id=id)
    if request.method == "POST":
        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.mobile = request.POST.get("mobile")
        student.email = request.POST.get("email")
        student.save()
        return redirect('student_list')

    data = {
        "student" : student
    }
    return render(request, "student_edit.html", data)

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("student_list")

from django.contrib.auth.models import User
from django.contrib import messages

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password1   # auto hashed ✔
        )
        user.save()
        return redirect('login')

    return render(request, 'register.html')

from django.contrib.auth import authenticate, login
def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    return render(request, 'login.html')

from django.contrib.auth import logout
from django.shortcuts import redirect

def user_logout(request):
    logout(request)          # ❌ destroys session
    return redirect('login') # redirect to login page