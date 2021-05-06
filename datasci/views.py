from django.shortcuts import render

from django.contrib.auth.models import User

from .forms import UserForm, ContactForm

from .models import Contact

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
