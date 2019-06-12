from django.db import models
from django.urls import reverse


class Osoba(models.Model):
    imie = models.CharField(max_length=50)
    nazwisko = models.CharField(max_length=50)

    def __str__(self):
        osoba = self.imie + " " + self.nazwisko
        return self.osoba

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})


class Telefon(models.Model):
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE, editable=False, null=True, related_name='telefony')
    telefon = models.CharField(max_length=50)

    def __str__(self):
        return self.telefon

    def get_absolute_url(self, telefon):
        pass

        #return reverse("detail", kwargs={"pk":Telefon.objects.get(telefon=self.telefon).osoba.id})



class Email(models.Model):
    osoba = models.ForeignKey(Osoba, on_delete=models.CASCADE, editable=False, null=True, related_name='maile')
    email = models.EmailField()

    def __str__(self):
        return self

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk":self.pk})
