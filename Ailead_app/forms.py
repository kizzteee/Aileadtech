from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormName(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    email = forms.EmailField(label='Your e-mail address', widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    subject = forms.CharField(max_length=100, widget=forms.TextInput(attrs={ 'class': 'form-control' }))
    message = forms.CharField(required=False, widget=forms.Textarea(attrs={ 'class': 'form-control' }))
