# Generated by Django 3.2.4 on 2021-06-16 14:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_alter_cars_features'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200, verbose_name='first name')),
                ('last_name', models.CharField(max_length=200, verbose_name='last name')),
                ('car', models.IntegerField(verbose_name='car id')),
                ('customer_need', models.CharField(max_length=200, verbose_name='customer need')),
                ('car_title', models.CharField(max_length=200, verbose_name='car title')),
                ('city', models.CharField(max_length=200, verbose_name='city')),
                ('state', models.CharField(max_length=200, verbose_name='state')),
                ('email', models.EmailField(max_length=200, verbose_name='email')),
                ('phone', models.CharField(max_length=200, verbose_name='phone')),
                ('message', models.TextField(max_length=200, verbose_name='message')),
                ('user_id', models.IntegerField(blank=True, verbose_name='user id')),
                ('create_data', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.AlterField(
            model_name='cars',
            name='vin_no',
            field=models.CharField(max_length=150, verbose_name='vin'),
        ),
    ]