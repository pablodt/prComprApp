from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission, User
import string
import random

def generate_unique_code_house():

    while True:
        while True:
            code = ''.join(random.choices(string.ascii_uppercase, k=6))
            if House.objects.filter(code=code).count() == 0:
                break

    return code

def generate_unique_code_product():

    while True:
        while True:
            code = ''.join(random.choices(string.ascii_uppercase, k=4))
            if Product.objects.filter(code=code).count() == 0:
                break

    return code

class PurchasingUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    
    groups = models.ManyToManyField(
        Group,
        related_name='purchasing_users',  # Cambia 'purchasing_users' a lo que prefieras
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='purchasing_users_permissions',  # Cambia 'purchasing_users_permissions' a lo que prefieras
        blank=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

    def __str__(self):
        return "{}".format(self.email)


class House(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code_house, unique=True)
    owner = models.ForeignKey(PurchasingUser, on_delete=models.CASCADE)


class Membership(models.Model):
    user = models.ForeignKey(PurchasingUser, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class SuperMarket(models.Model):
    name = models.CharField(max_length=60)
    house = models.ForeignKey(House, on_delete=models.CASCADE)


class Product(models.Model):
    code = models.CharField(max_length=8, default=generate_unique_code_product, unique=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=8)
    supermarket = models.ForeignKey(SuperMarket, on_delete=models.CASCADE)
    stock = models.IntegerField()