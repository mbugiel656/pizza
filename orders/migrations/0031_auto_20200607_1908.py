# Generated by Django 2.2.7 on 2020-06-07 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0030_auto_20200601_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='email',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='name',
        ),
    ]
