# Generated by Django 2.2.7 on 2019-11-27 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_price',
            new_name='pizza_lg_price',
        ),
        migrations.AddField(
            model_name='pizza',
            name='pizza_sm_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=4),
        ),
    ]
