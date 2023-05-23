from rest_framework import serializers
from .models import Product, Card, Brand, Rate

class RateSerializer(serializers.ModelSerializer):
    one_star = serializers.IntegerField(read_only=False)
    class Meta:
        model = Rate
        fields = (
            'id',
            'one_star',
            'two_star',
            'three_star',
            'four_star',
            'five_star',
            'total_rate_count',
            'total_rate',
            'average_rate'
        )

class ProductSerializer(serializers.ModelSerializer):
    ratings = RateSerializer(many=True, read_only=True)
    lookup_field = "name"
    class Meta:
        model = Product
        fields = (
            "id",
            "name",
            "price",
            "view_count",
            "quantity",
            "brand",
            #"imageURL",
            "ratings"
        )

class CardSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Card
        fields = (
            "id",
            "user",
            "product",
            "quantity"       
        )

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = (
            "id",
            "name"
        )