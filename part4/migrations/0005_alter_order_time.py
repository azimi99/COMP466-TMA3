# Generated by Django 4.0.4 on 2022-05-27 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('part4', '0004_alter_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]