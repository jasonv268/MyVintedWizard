# Generated by Django 4.2.9 on 2024-01-11 19:21

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters_manager', '0002_alter_filter_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='colors',
            field=models.JSONField(choices=[('BLACK', 'BLACK'), ('WHITE', 'WHITE'), ('GREY', 'GREY'), ('BLUE', 'BLUE'), ('GREEN', 'GREEN'), ('YELLOW', 'YELLOW'), ('PURPLE', 'PURPLE')], default={}),
        ),
        migrations.AddField(
            model_name='article',
            name='sizes',
            field=models.JSONField(choices=[('MEN,XS', 'MEN,XS'), ('MEN,S', 'MEN,S'), ('MEN,M', 'MEN,M'), ('MEN,L', 'MEN,L'), ('MEN,XL', 'MEN,XL'), ('WOMEN,XXS', 'WOMEN,XXS'), ('WOMEN,XXS', 'WOMEN,XXS'), ('WOMEN,XS', 'WOMEN,XS'), ('WOMEN,S', 'WOMEN,S'), ('WOMEN,M', 'WOMEN,M'), ('WOMEN,L', 'WOMEN,L'), ('WOMEN,XL', 'WOMEN,XL'), ('CHILDREN,10A', 'CHILDREN,10A'), ('CHILDREN,11A', 'CHILDREN,11A'), ('CHILDREN,12A', 'CHILDREN,12A'), ('CHILDREN,13A', 'CHILDREN,13A'), ('CHILDREN,14A', 'CHILDREN,14A'), ('CHILDREN,15A', 'CHILDREN,15A'), ('CHILDREN,16A', 'CHILDREN,16A')], default={}),
        ),
        migrations.AlterField(
            model_name='filter',
            name='price_max',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='filter',
            name='price_min',
            field=models.FloatField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
