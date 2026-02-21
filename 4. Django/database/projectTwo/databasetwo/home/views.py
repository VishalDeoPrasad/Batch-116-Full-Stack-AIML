from django.shortcuts import render
from home.forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            mobile = form.cleaned_data['mobile']
            message = form.cleaned_data['message']
            
            print(name, email, mobile, message)

    form = ContactForm()
    return render(request, 'contact.html', {'form':form})