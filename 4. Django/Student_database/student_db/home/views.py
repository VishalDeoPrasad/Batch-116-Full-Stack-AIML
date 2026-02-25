from django.shortcuts import render, redirect
from home.models import Student
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "home.html")

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

def student_list(request):
    query = request.GET.get('query')
    if query:
        # students = Student.objects.filter(name=query)
        students = Student.objects.filter(Q(name__icontains=query))
    else:
        students = Student.objects.all()

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

    data = {
        "student" : student
    }
    return render(request, "student_edit.html", data)

def student_delete(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect("student_list")

def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        useremail = request.POST.get('useremail')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username,
                                 email=useremail,
                                 password=password)
        user.save()
        return redirect("login")
        
    return render(request, "register.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("home")
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")