# Generated by Django 2.2.7 on 2019-12-11 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0008_auto_20191211_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='subshoppingcart',
            name='sub_topping_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
