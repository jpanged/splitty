# Generated by Django 2.0.1 on 2018-02-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopperHelper', '0005_auto_20180204_0000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='user_Type',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='first_Name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_Name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
