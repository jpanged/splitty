# Generated by Django 2.0.2 on 2018-02-04 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopperHelper', '0002_auto_20180204_0141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(max_length=10),
        ),
    ]