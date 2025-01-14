from django.db import models

# Create your models here.

class Buyer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
    age = models.IntegerField(max_length=3)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=50, unique=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer)


