# Generated by Django 2.2.7 on 2019-12-11 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_subshoppingcart_toppings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subshoppingcart',
            old_name='sub_topping_price',
            new_name='sub_toppings_price',
        ),
    ]
