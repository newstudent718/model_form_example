from django.forms import ModelForm
from django.contrib.auth.models import User

from .models import Contact, About

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class AboutForm(ModelForm):
    class Meta:
        model = About
        fields = '__all__'
