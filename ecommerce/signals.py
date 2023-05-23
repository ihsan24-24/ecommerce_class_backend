from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Rate, Product

@receiver(post_save, sender=Product)
def create_product_rating(sender, instance, created, **kwargs):
    if created:
        Rate.objects.create(product=instance)
        print("çalıştı")