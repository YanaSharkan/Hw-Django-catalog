from django.db import models


class City(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Retailer(models.Model):
    name = models.CharField(max_length=200)
    city = models.OneToOneField(City, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    retailer = models.ForeignKey(Retailer, null=True, on_delete=models.SET_NULL)
    description = models.TextField()

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.ForeignKey(City, null=True, on_delete=models.SET_NULL)
    products = models.ManyToManyField(Product, verbose_name="list of products")

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)
