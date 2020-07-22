from django.db import models
from django.core import validators
from django.core.exceptions import ValidationError

# Create your models here.

class Orders(models.Model):

    def no_spaces(value):
        if ' ' in value:
            raise ValidationError('Name cannot contain spaces')

    first_name = models.CharField(max_length=30, validators=[no_spaces])
    last_name = models.CharField(max_length=30, validators=[no_spaces])
    phone = models.CharField(max_length=12, validators=[validators.MinLengthValidator(10)])
    email = models.EmailField()
    company = models.CharField(max_length=200)
    address = models.CharField(max_length=400)

    val_1 = models.IntegerField()
    qty_1 = models.IntegerField()
    val_2 = models.IntegerField(blank=True, null=True)
    qty_2 = models.IntegerField(blank=True, null=True)
    val_3 = models.IntegerField(blank=True, null=True)
    qty_3 = models.IntegerField(blank=True, null=True)
    val_4 = models.IntegerField(blank=True, null=True)
    qty_4 = models.IntegerField(blank=True, null=True)
    val_5 = models.IntegerField(blank=True, null=True)
    qty_5 = models.IntegerField(blank=True, null=True)
    val_6 = models.IntegerField(blank=True, null=True)
    qty_6 = models.IntegerField(blank=True, null=True)
    val_7 = models.IntegerField(blank=True, null=True)
    qty_7 = models.IntegerField(blank=True, null=True)
    val_8 = models.IntegerField(blank=True, null=True)
    qty_8 = models.IntegerField(blank=True, null=True)

    order_date = models.DateTimeField(auto_now_add=True)
    order_number = models.CharField(max_length=8, blank=True, null=True)
    order_status = models.CharField(max_length=12, blank=True, null=True)
    payment_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return '{} {} - {}'.format(self.first_name, self.last_name, self.company)
