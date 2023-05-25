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
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="cards", blank=True)

class CardProduct(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="products")
    quantity = models.PositiveIntegerField(default=1)

status = (
    (1, "Preparing"),
    (2, "on way"),
    (3, "has been delivered")
)
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="orders", blank=True)
    card = models.OneToOneField(Card, on_delete=models.CASCADE, related_name="orders", blank=True)
    status = models.PositiveSmallIntegerField(choices=status, default=1)
