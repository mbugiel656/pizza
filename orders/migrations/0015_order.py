# Generated by Django 2.2.7 on 2020-05-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0014_auto_20200508_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(default='none', max_length=128)),
                ('ordered_items', models.CharField(default='none', max_length=256)),
                ('order_time', models.CharField(default='none', max_length=32)),
                ('total_cost', models.CharField(default='none', max_length=32)),
            ],
        ),
    ]
