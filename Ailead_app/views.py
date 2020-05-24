from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.template.loader import get_template



@login_required(login_url='login')
def home(request):
    return render(request, 'Ailead_app/index.html')

@login_required(login_url='login')
def courses(request):
    return render(request, 'Ailead_app/courses.html')

@login_required(login_url='login')
def about(request):
    return render(request, 'Ailead_app/about.html')

@login_required(login_url='login')
def contact(request):
    Contact_Form = ContactForm
    if request.method == 'POST':
        form = Contact_Form(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name')
            contact_email = request.POST.get('contact_email')
            contact_content = request.POST.get('content')

            template = get_template('Ailead_app/contact_form.txt')
            context = {
                'contact_name' : contact_name,
                'contact_email' : contact_email,
                'contact_content' : contact_content,
            }

            content = template.render(context)

            email = EmailMessage(
                "New contact form email",
                content,
                "Creative web" + '',
                ['example@gmail.com'],
                headers = { 'Reply To': contact_email }
            )

            email.send()

            return render(request, 'Ailead_app/success.html')
    return render(request, 'Ailead_app/contact.html', {'form':Contact_Form })

def success(request):
    context = {}
    return render(request, 'Ailead_app/success.html', context)

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username or Password is incorrect')

    context = {}
    return render(request, 'Ailead_app/login.html', context)

def Logout_user(request):
    logout(request)
    return redirect('login')

def register(request):

    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for'+ user )
            return redirect('login')

    context = {'form':form}
    return render(request, 'Ailead_app/register.html', context)

def whatsnew(request):
    context = {}
    return render(request, 'Ailead_app/whatsnew.html', context)
