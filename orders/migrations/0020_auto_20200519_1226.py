# Generated by Django 2.2.7 on 2020-05-19 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0019_auto_20200518_2302'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcart',
            name='order_confirmed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='shoppingcart',
            name='order_time',
            field=models.CharField(default='', max_length=128),
        ),
    ]
