# Generated by Django 3.0.7 on 2022-05-06 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='is_bought',
            field=models.BooleanField(default=False),
        ),
    ]
