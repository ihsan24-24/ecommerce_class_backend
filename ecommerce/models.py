from django.db import models
from django.contrib.auth.models import User

class Brand(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    name = models.CharField(max_length=25)
    #imageURL = models.URLField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    view_count = models.PositiveIntegerField(default=0)
    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name}"
    
class Rate(models.Model):
    product = models.ForeignKey(Product, related_name='ratings', on_delete=models.CASCADE)
    one_star = models.IntegerField(default=0)
    two_star = models.IntegerField(default=0)
    three_star = models.IntegerField(default=0)
    four_star = models.IntegerField(default=0)
    five_star = models.IntegerField(default=0)
    total_rate_count = models.IntegerField(default=0)
    total_rate = models.IntegerField(default=0)
    average_rate = models.DecimalField(max_digits=2, decimal_places=1, default=0.0)

    def __str__(self):
        return f"{self.average_rate}"
class Card(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(User, related_name="cards", on_delete=models.CASCADE, blank=True)

