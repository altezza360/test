from django.db import models
from django.contrib.auth.models import User

class Manager(models.Model):
    pass

class Specialist(models.Model):
    SPECIALITY = [
        ('elektrik', 'elektrik'),
        ('plotnik', 'plotnik'),
        ('svarshik', 'svarshik')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="specialist", null=True)
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField(null=True)
    speciality = models.CharField(max_length=200, null=True, choices=SPECIALITY)

    def __str__(self):
        return self.name


class Product(models.Model):
    CATEGORY = (
        ('derevo', 'derevo'),
        ('metal', 'metal'),
        ('dostavka', 'dostavka')
    )
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=1000, null=True)
    price = models.FloatField(null=True)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=30, null=True)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    STATUS = (
        ('pending', 'pending'),
        ('order in process', 'order in process'),
        ('delivered', 'delivered')
    )

    description = models.CharField(max_length=500, null=True)
    specialist = models.ForeignKey(Specialist, null=True, on_delete=models.SET_NULL)
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    price = models.IntegerField(null=True)
    deposit = models.IntegerField(null=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.description


