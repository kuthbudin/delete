from django.db import models

# Create your models here.
class RegistrationModel(models.Model):
    name = models.CharField(max_length=15)
    contact = models.IntegerField(max_length=10)
    password = models.CharField(max_length=12)
    repassword = models.CharField(max_length=12)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name + " : " + self.email
