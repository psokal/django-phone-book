from django import forms
from django.forms import ModelForm
from .models import Telefon, Osoba, Email

class TelefonForm(forms.ModelForm):
    telefon = forms.CharField()

    class Meta:
        model = Telefon
        fields = ("telefon",)

class EmailForm(forms.ModelForm):
    email = forms.CharField()

    class Meta:
        model = Email
        fields = ("email",)
