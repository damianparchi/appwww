# Generated by Django 4.1.2 on 2022-10-19 18:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appka', '0003_alter_osoba_data_dodania_alter_osoba_miesiac'),
    ]

    operations = [
        migrations.AlterField(
            model_name='osoba',
            name='data_dodania',
            field=models.DateField(default=datetime.datetime(2022, 10, 19, 20, 16, 1, 140931)),
        ),
    ]
