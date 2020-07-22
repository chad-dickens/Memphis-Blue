# Generated by Django 3.0.3 on 2020-07-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_cards_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='phone',
            field=models.CharField(default='null', max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='orders',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]