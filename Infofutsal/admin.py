from django.contrib import admin
from .models.contact import Contact
from .models.review import Review

# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'subject', 'message']

admin.site.register(Contact , AdminContact)

class AdminReview(admin.ModelAdmin):
    list_display = ['fullname', 'message']

admin.site.register(Review , AdminReview)