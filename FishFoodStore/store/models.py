from django.db import models
from django.core import validators

# Create your models here.
class Customer(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = models.PositiveIntegerField()
    district = models.CharField(max_length=50)
    streetName = models.CharField(max_length=50)
    buildingNumber = models.PositiveIntegerField()
    additionalInfo = models.TextField()
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    cart = models.ManyToManyField('Product', blank=True)

class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Processing', 'Processing'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    status = models.CharField(max_length=200, choices=STATUS_CHOICES, default='Pending')
    total = models.DecimalField(max_digits=8, decimal_places=2, default=0.00)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=8, decimal_places=2)