# Generated by Django 3.2.4 on 2021-06-16 15:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_alter_message_car'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='cars.cars', verbose_name='car id'),
        ),
    ]
