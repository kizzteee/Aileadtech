from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from . import forms
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm, ContactForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, get_connection, BadHeaderError
from django.template.loader import get_template
from django.urls import reverse




def home(request):
    context ={}
    return render(request, 'Ailead_app/index.html', context)


def courses(request):
    return render(request, 'Ailead_app/courses.html')


def about(request):
    return render(request, 'Ailead_app/about.html')

@login_required
def user_logout(request):
    # Log out the user.
    logout(request)
    # Return to homepage.
    return render(request, 'Ailead_app/index.html')


def contact(request):
    submitted = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
             # assert False

            send_mail(
                cd['subject'],
                cd['message'],
                cd['email'],
                ['kizzyiyke4@gmail.com'],
             )
            return HttpResponseRedirect('/contact?submitted=True')
    else:
        form = ContactForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'Ailead_app/contact.html', {'form': form, 'submitted': submitted})

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
def ecommerce(request):
    context = {}
    return render(request, 'Ailead_app/ecommerce.html', context)
