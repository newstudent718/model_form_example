from django.shortcuts import render

from django.contrib.auth.models import User

from .forms import UserForm, ContactForm, AboutForm

from .models import Contact, About

def index(request):
    users = User.objects.all()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = UserForm
    return render(request, 'index.html', context={'users':users, 'form': form})

def contact(request):
    c = Contact.objects.all()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm

    return render(request, 'contact.html', context={'contacts': c, 'form': form})

def about(request):
    a = About.objects.first()
    if request.method == 'POST':
        form = AboutForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AboutForm
    return render(request, 'about.html', context={'a': a, 'form': form})

