# Generated by Django 3.0.3 on 2020-07-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_cards_app', '0005_auto_20200719_0659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_number',
            field=models.CharField(blank=True, max_length=8, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='qty_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='qty_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='qty_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='qty_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='qty_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='qty_7',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='qty_8',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='val_2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='val_3',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='val_4',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='val_5',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='val_6',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='val_7',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='val_8',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
