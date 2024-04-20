import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','crudDemo.settings')

import django
django.setup()

from crudApp.models import*
from faker import Faker
from random import *
faker = Faker()

def generate(n):
    for i in range(n):
        fsno = randint(1001,9999)
        fsname = faker.name()
        fsclass = randint(1,10)
        fsadress = faker.city()
        stud_record = student.objects.get_or_create(sno=fsno,sname=fsname,sclass=fsclass,sadress=fsadress)
generate(30)