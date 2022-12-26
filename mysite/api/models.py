from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    avatar = models.ImageField(upload_to='api/images/avatars', blank=False)


class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='api/images/products')
    description = models.CharField(max_length=2500)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(AdvUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.name
