# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

MANAGED = True


class Areas(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    government = models.CharField(max_length=255, blank=True, null=True)


    def __unicode__(self):
        return self.name

    class Meta:
        managed = MANAGED
        db_table = 'areas'


class Customers(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    account_number = models.CharField(max_length=45, blank=True, null=True)
    is_customer = models.BooleanField(default=True)
    areas = models.ForeignKey(Areas,models.CASCADE, related_name='area_customer', db_column='area_id')

    def __unicode__(self):
        return self.name

    class Meta:
        managed = MANAGED
        db_table = 'customers'


class Invoice(models.Model):
    invoice_date = models.DateTimeField(blank=True, null=True)
    area = models.ForeignKey(Areas, models.CASCADE, blank=True, null=True)
    customer = models.ForeignKey(Customers, models.CASCADE, blank=True, null=True, related_name='invoice_customer')
    car_number = models.CharField(max_length=45, blank=True, null=True)
    car_owner = models.ForeignKey(Customers, models.CASCADE, db_column='car_owner', related_name='car_owner',
                                  blank=True, null=True)
    car_driver = models.CharField(max_length=45, blank=True, null=True)
    invoice_number = models.CharField(max_length=45)
    delivery_distnation = models.CharField(max_length=255)
    # created_by = models.ForeignKey(User)

    def __unicode__(self):
        return str(self.id) + ":" + str(self.invoice_date)




    class Meta:
        managed = MANAGED
        db_table = 'invoice'


class InvoiceLine(models.Model):
    invoice = models.ForeignKey(Invoice, models.CASCADE, blank=True, null=True, related_name='line')
    item = models.ForeignKey('Items', models.CASCADE, blank=True, null=True, related_name='items')
    qantity = models.FloatField(blank=True, null=True)


    class Meta:
        managed = MANAGED
        db_table = 'invoice_line'


class Items(models.Model):
    name = models.CharField(max_length=45, blank=True, null=True)
    price = models.FloatField(blank=True, null=True)
    price_refactor = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return self.name

    class Meta:
        managed = MANAGED
        db_table = 'items'
