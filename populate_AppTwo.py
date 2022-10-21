import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

#SCRIPT
import random
from AppTwo.models import User
from faker import Faker

faking = Faker()

def populate(N = 5):
    for entry in range(N):
        fake_name = faking.name().split()
        fake_first = fake_name[0]
        fake_last =fake_name[1]
        fake_email = faking.email()

        us = User.objects.get_or_create(First_Name = fake_first ,
                                        Last_Name = fake_last ,
                                         Email = fake_email)[0]

if __name__ == '__main__':
    print("Populating Script!!")
    populate(20)
    print("Populating Complete!!")
