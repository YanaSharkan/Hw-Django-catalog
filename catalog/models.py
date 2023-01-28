from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)


class Retailer(models.Model):
    name = models.CharField(max_length=200)
    city = models.OneToOneField(City, null=True, on_delete=models.SET_NULL)


class Product(models.Model):
    name = models.CharField(max_length=200)
    retailer = models.ForeignKey(Retailer, null=True, on_delete=models.SET_NULL)
    description = models.TextField()


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    products = models.ManyToManyField(Product, verbose_name="list of products")
