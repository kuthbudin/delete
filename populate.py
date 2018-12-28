import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'views.settings')
import django
django.setup()

from faker import Faker
from random import *
from fviews.models import RegistrationModel

faker=Faker()
def populate(n):
    for i in range(n):
        x=randint(1001,9999)
        name = faker.name()
        password = faker.city()
        repassword = password
        contact = randint(9001,99999)
        email = faker.email()
        emp_record = RegistrationModel.objects.get_or_create(name=name, password=password, repassword=password, email=email, contact=contact)


populate(5)