# Generated by Django 4.2.9 on 2024-01-13 09:59

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filters_manager', '0009_alter_article_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sizes',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('a', 'A'), ('b', 'B')], max_length=3),
        ),
    ]
