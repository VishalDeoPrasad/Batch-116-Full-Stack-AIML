from django.shortcuts import render, redirect
from home.models import Register

def home(request):
    return render(request, "home.html")

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = Register.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            return redirect("dashboard")
            
        except Register.DoesNotExist:
            context = {
                "message": "Invalid Credentials!"
            }
            return render(request, "login.html", context)
        
        
    return render(request, "login.html")

def register(request):
    if request.method == "POST":
        fullname = request.POST.get("fullname")
        displayname = request.POST.get("displayname")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        city = request.POST.get("city")
        date = request.POST.get("date")
        password = request.POST.get("password")
        image = request.FILES['image']
        # print(fullname, displayname, email, contact, 
        #       city, date, password, image)

        Register.objects.create(
            name = fullname,
            display_name = displayname,
            email = email,
            contact = contact,
            city = city,
            dob = date,
            password = password,
            image = image
        )
        return redirect("login")
        
    return render(request, "register.html")

def logout(request):
    if "user_id" in request.session:
        del request.session['user_id']
    return redirect("login")

def dashboard(request):
    id = request.session.get("user_id")
    if not id:
        return redirect("login")
    user = Register.objects.get(id=id)

    return render(request, "dashboard.html", {"user": user})