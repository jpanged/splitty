# Generated by Django 2.0.1 on 2018-02-04 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopperHelper', '0003_auto_20180203_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]
