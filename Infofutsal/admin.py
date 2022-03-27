from django.contrib import admin
from .models.contact import Contact

# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'subject', 'message']

admin.site.register(Contact , AdminContact)