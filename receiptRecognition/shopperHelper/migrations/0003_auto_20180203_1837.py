# Generated by Django 2.0.1 on 2018-02-04 02:37

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('shopperHelper', '0002_auto_20180203_1807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
