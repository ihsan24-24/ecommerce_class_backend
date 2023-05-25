from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from rest_framework.decorators import api_view
from decimal import Decimal
from .models import Product, Card, Brand, Rate, CardProduct
from .serializers import ProductSerializer, CardSerializer, BrandSerializer, RateSerializer, CardProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'name'

    def get_queryset(self, name=None):
        if name:
            return Product.objects.filter(name=name)
        return Product.objects.all()
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.view_count += 1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

class BrandViewSet(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class CreateCardProductViewSet(viewsets.ViewSet):
    def create(self, request):
        product_id = request.data.get('product_id')
        user = request.user

        # Eğer kullanıcının bir card'ı yoksa, card verisini oluştur
        try:
            card = Card.objects.get(user=user)
        except Card.DoesNotExist:
            card = Card.objects.create(user=user)

        # CardProduct'u kontrol et eğer product daha önce card'a eklenmiş ise quantity artır eklenmemişse create et
        try:
            card_product = CardProduct.objects.filter(card=card, product_id=product_id).first()

            if len(card_product) > 0:
                card_product.quantity += 1
                card_product.save()
            else:
                product = Product.objects.get(id=product_id)
                card_product = CardProduct.objects.create(card=card, product=product)

            serializer = CardProductSerializer(card_product)
            return Response(serializer.data)

        except Product.DoesNotExist:
            return Response({'message': 'Invalid product'}, status=400)


class DeleteCardProductViewSet(viewsets.ViewSet):
    def delete_card_product(self, request):
        product_id = request.data.get('product_id')
        user = request.user
        # User'ın card bilgisini alıyoruz. Eğer kullanıcının bir card'ı yoksa, invalid card hatası dönüyoruz
        try:
            card = Card.objects.get(user=user)
        except Card.DoesNotExist:
            return Response({'message': 'Invalid card product'}, status=400)

        try:
            card_product = CardProduct.objects.get(card_id=card.id, product_id=product_id)

            # eğer card'dan çıkarılmak istenen ürünün quantity 1 den büyük ise quantity 1 eksilt eğer 1 ise sil
            if card_product.quantity > 1:
                card_product.quantity -= 1
                card_product.save()
            else:
                card_product.delete()

            return Response({'message': 'Card product deleted successfully'})

        except CardProduct.DoesNotExist:
            return Response({'message': 'Invalid card product'}, status=400)

class RateUpdateView(generics.UpdateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        # gelen yıldız değerine göre rating'i artırıyoruz
        one_star = request.data.get('one_star')
        two_star = request.data.get('two_star')
        three_star = request.data.get('three_star')
        four_star = request.data.get('four_star')
        five_star = request.data.get('five_star')
        if one_star is not None:
            request.data.pop('one_star', None)
            instance.one_star += 1
            instance.total_rate_count += 1
            instance.total_rate += 1
            instance.average_rate = Decimal(instance.total_rate) / instance.total_rate_count
            instance.average_rate = instance.average_rate.quantize(Decimal('0.0'))  # Yuvarlama işlemi
            instance.save()
        elif two_star is not None:
            instance.two_star += 1
            instance.total_rate_count += 1
            instance.total_rate += 2
            instance.average_rate = Decimal(instance.total_rate) / instance.total_rate_count
            instance.average_rate = instance.average_rate.quantize(Decimal('0.0'))  # Yuvarlama işlemi
            instance.save()
        elif three_star is not None:
            instance.three_star += 1
            instance.total_rate_count += 1
            instance.total_rate += 3
            instance.average_rate = Decimal(instance.total_rate) / instance.total_rate_count
            instance.average_rate = instance.average_rate.quantize(Decimal('0.0'))  # Yuvarlama işlemi
            instance.save()
        elif four_star is not None:
            instance.four_star += 1
            instance.total_rate_count += 1
            instance.total_rate += 4
            instance.average_rate = Decimal(instance.total_rate) / instance.total_rate_count
            instance.average_rate = instance.average_rate.quantize(Decimal('0.0'))  # Yuvarlama işlemi
            instance.save()
        elif five_star is not None:
            instance.five_star += 1
            instance.total_rate_count += 1
            instance.total_rate += 5
            instance.average_rate = Decimal(instance.total_rate) / instance.total_rate_count
            instance.average_rate = instance.average_rate.quantize(Decimal('0.0'))  # Yuvarlama işlemi
            instance.save()

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)    

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

# class DeleteRating(generics.DestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
