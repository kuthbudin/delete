from faker import Faker
from random import *
faker=Faker()

def populate(n):
    for i in range(n):
        x=randint(1001,9999)
        name = faker.name()
        password = faker.city()
        repassword = password
        contact = randint(9001,99999)

