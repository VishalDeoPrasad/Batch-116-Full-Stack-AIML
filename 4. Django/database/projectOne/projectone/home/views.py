from django.shortcuts import render
from home.models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
       name = request.POST.get('name')
       mobile = request.POST.get('mobile')
       email = request.POST.get('email')
       msg = request.POST.get('msg')
       #print(name, mobile, email, msg)

       Contact.objects.create(
           name = name,
           mobile = mobile,
           email = email,
           message = msg
        )
    return render(request, 'contact.html')

def contact_list(request):
    contacts = Contact.objects.all()
    data = {
        "contacts":contacts
    }
    return render(request, "contact_list.html", data)