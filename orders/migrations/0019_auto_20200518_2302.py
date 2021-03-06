# Generated by Django 2.2.7 on 2020-05-18 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0018_auto_20200518_2111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shoppingcart',
            name='order_confirmed',
        ),
        migrations.RemoveField(
            model_name='shoppingcart',
            name='order_time',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_time',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='order',
            name='ordered_items',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='order',
            name='total_cost',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='order',
            name='user',
            field=models.CharField(default='', max_length=128),
        ),
    ]
