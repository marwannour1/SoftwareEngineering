from django.db import models
from django.urls import reverse
from django.core.validators import MinLengthValidator

# Create your models here.
class Customer(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=100)
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    phone = models.CharField(max_length=11, validators=[MinLengthValidator(11)])
    district = models.CharField(max_length=50)
    streetName = models.CharField(max_length=50)
    buildingNumber = models.PositiveIntegerField()
    additionalInfo = models.TextField()
    ordered = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    
    def __str__(self) -> str:
        return f"{self.firstName} {self.lastName}"

class Product(models.Model):
    name = models.CharField(max_length=64)
    price = models.PositiveIntegerField()
    quantity = models.IntegerField()
    customer = models.ManyToManyField(Customer, blank=True, related_name="customers")