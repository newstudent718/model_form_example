from django.contrib.auth.models import User
from django.db import models

User._meta.get_field('email')._unique = True

class Contact(models.Model):
    email = models.EmailField(max_length=50, unique=False)
    message = models.TextField()

    def __str__(self):
        return f"<Contact email={self.email}>"

class About(models.Model):
    blurb = models.TextField()
    pic = models.FileField(upload_to='')
