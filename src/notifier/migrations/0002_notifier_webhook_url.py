# Generated by Django 4.2.9 on 2024-03-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifier', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifier',
            name='webhook_url',
            field=models.CharField(default='https://discord.com/api/webhooks/1210161827812478976/eg61-n6r2mDv5vKNH2ScP0hz7EPo-5kDjoL10kKqbrK_VKVDRpvGgK9kAaA2xfIWWjtH', max_length=180),
            preserve_default=False,
        ),
    ]
