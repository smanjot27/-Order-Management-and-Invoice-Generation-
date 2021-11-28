from django.db import models

# Create your models here.
class Order(models.Model):
    Order_id=models.AutoField(primary_key=True)
    serial_number=models.CharField(max_length=50)
    order_name=models.CharField(max_length=160)
    amount=models.IntegerField()
    salesman_assigned=models.CharField(max_length=100)
    delivery_date=models.DateField()
    mobile_number=models.CharField(max_length=12)
    tailor_assigned=models.CharField(max_length=100)
    advance=models.IntegerField()
    order_received=models.DateField(auto_now=True)

class tailor(models.Model):
    tailorid=models.AutoField(primary_key=True)
    tailor_name=models.CharField(max_length=20)

class Completed(models.Model):
    Order_id=models.AutoField(primary_key=True)
    serial_number=models.CharField(max_length=50)
    order_name=models.CharField(max_length=160)
    amount=models.IntegerField()
    salesman_assigned=models.CharField(max_length=100)
    booking_date=models.DateField()
    mobile_number=models.CharField(max_length=12)
    tailor_assigned=models.CharField(max_length=100)
    advance=models.IntegerField()
    order_completed=models.DateField(auto_now=True)
