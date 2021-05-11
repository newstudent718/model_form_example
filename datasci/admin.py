from django.contrib import admin

from .models import Contact, About

class ContactModel(admin.ModelAdmin):
    pass

class AboutModel(admin.ModelAdmin):
    pass

admin.site.register(Contact, ContactModel)
admin.site.register(About, AboutModel)
