from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, min_length=3, required=True)
    email = forms.EmailField(required=True)
    mobile = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea)