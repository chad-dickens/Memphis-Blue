# Generated by Django 3.0.3 on 2020-07-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_cards_app', '0002_auto_20200716_1156'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address',
            field=models.CharField(default='null', max_length=400),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orders',
            name='company',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
