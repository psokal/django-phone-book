# Generated by Django 2.2.1 on 2019-06-08 21:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Osoba',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=50)),
                ('nazwisko', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Telefon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.CharField(max_length=50)),
                ('osoba', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='phone_book_app.Osoba')),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('osoba', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='phone_book_app.Osoba')),
            ],
        ),
    ]
