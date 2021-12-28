from django.db import models

# Create your models here.
class Order(models.Model):
    Order_id=models.AutoField(primary_key=True)
    serial_number=models.CharField(max_length=50)
    order_name=models.CharField(max_length=160,blank=True)
    amount=models.IntegerField(blank=True, null=True)
    salesman_assigned=models.CharField(max_length=100, blank=True)
    delivery_date=models.DateField(blank=True, null=True)
    mobile_number=models.CharField(max_length=12,blank=True)
    tailor_assigned=models.CharField(max_length=100,blank=True)
    advance=models.IntegerField(blank=True, null=True)
    order_received=models.DateField(auto_now=True)

class tailor(models.Model):
    tailorid=models.AutoField(primary_key=True)
    serial_no=models.CharField(max_length=50)
    tailor_name=models.CharField(max_length=20)

class Completed(models.Model):
    Order_id=models.AutoField(primary_key=True)
    serial_number=models.CharField(max_length=50)
    order_name=models.CharField(max_length=160,blank=True)
    amount=models.IntegerField(blank=True, null=True)
    salesman_assigned=models.CharField(max_length=100, blank=True)
    booking_date=models.DateField(blank=True)
    mobile_number=models.CharField(max_length=12,blank=True)
    tailor_assigned=models.CharField(max_length=100,blank=True)
    advance=models.IntegerField(blank=True, null=True)
    order_completed=models.DateField(auto_now=True)
