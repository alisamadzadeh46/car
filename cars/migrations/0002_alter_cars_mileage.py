# Generated by Django 3.2.4 on 2021-06-09 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='mileage',
            field=models.IntegerField(verbose_name='mileage'),
        ),
    ]
