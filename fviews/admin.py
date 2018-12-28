from django.contrib import admin
from fviews.models import RegistrationModel

# Register your models here.
class RegistraionModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'contact', 'password', 'email']

admin.site.register(RegistrationModel, RegistraionModelAdmin)
