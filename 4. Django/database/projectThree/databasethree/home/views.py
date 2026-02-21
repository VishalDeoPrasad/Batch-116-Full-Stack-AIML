from django.shortcuts import render
from home.forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, "contact.html", {"form":form})