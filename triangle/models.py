from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Log(models.Model):
    path = models.CharField(max_length=300)
    METHODS = [
        ('GET', 'GET'),
        ('POST', 'POST'),
        ('PUT', 'PUT'),
        ('DELETE', 'DELETE'),
        ('PATCH', 'PATCH')
    ]
    method = models.CharField(max_length=6, choices=METHODS)
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.JSONField()
    query = models.JSONField(default=dict())

    def __str__(self):
        return f'{self.method} {self.path}'
