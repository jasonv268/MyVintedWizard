# Generated by Django 4.2.9 on 2024-01-13 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filters_manager', '0008_alter_article_colors_alter_article_sizes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='sizes',
            field=models.JSONField(choices=[('a', 'A'), ('b', 'B')]),
        ),
    ]
