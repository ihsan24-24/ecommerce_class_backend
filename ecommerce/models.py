from django.db import models

class Brand(models.Model):
    name = models.CharField(max_length=25)

class Product(models.Model):
    name = models.CharField(max_length=25)
    imageURL = models.URLField()
    price = models.PositiveSmallIntegerField()
    brand = models.ForeignKey(Brand, related_name='products', on_delete=models.CASCADE)
    review = models.PositiveIntegerField(default=0)
    
class Rate(models.Model):
    product = models.ForeignKey(Product, related_name='rating', on_delete=models.CASCADE)
    oneStar = models.IntegerField(default=0)
    twoStar = models.IntegerField(default=0)
    threeStar = models.IntegerField(default=0)
    fourStar = models.IntegerField(default=0)
    fiveStar = models.IntegerField(default=0)
    totalRateCount = models.IntegerField(default=0)
    averageRateCount = models.IntegerField(default=0)
