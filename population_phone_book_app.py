import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','phone_book_project.settings')

import django

django.setup()

from random import randint

from phone_book_app.models import Osoba, Telefon, Email
from faker import Faker, Factory

fake = Factory.create('pl_PL')



def populate(N=5):

    for entry in range(N):

        fake_name = fake.first_name()
        fake_surname = fake.last_name()
        person = Osoba.objects.get_or_create(imie=fake_name, nazwisko=fake_surname)[0]
        i = randint(0, 4)
        for j in range(0, i):
            fake_phone = fake.phone_number()
            phone = Telefon.objects.get_or_create(osoba=person,telefon=fake_phone)[0]
        i = randint(0, 3)
        for j in range(0, i):
            fake_email = fake.email()
            email = Email.objects.get_or_create(osoba=person,email=fake_email)[0]


if __name__ == '__main__':
    print("Please Wait...")
    populate(25)
    print('Complete')
