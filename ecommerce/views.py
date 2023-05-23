from rest_framework.response import Response
from rest_framework import viewsets, generics, status
from decimal import Decimal
from .models import Product, Card, Brand, Rate
from .serializers import ProductSerializer, CardSerializer, BrandSerializer, RateSerializer

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

class CardCreateView(generics.CreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def create(self, request, *args, **kwargs):
        product_id = request.data.get('product')
        user_id = request.user.id

        # Kullanıcının card verilerini kontrol et
        existing_card = Card.objects.filter(user=user_id, product=product_id).first()

        if existing_card:
            
            # Eğer aynı ürün varsa quantity'yi bir artır
            existing_card.quantity += 1
            existing_card.save()
            serializer = self.get_serializer(existing_card)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            # Aynı ürün yoksa yeni card oluştur
            request.data['product'] = product_id
            request.data['user'] = user_id
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

class CardDeleteView(generics.UpdateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def update(self, request, *args, **kwargs):
        user_id = request.user.id
        product_id = request.data.get('product')

        # Kullanıcının card verilerini kontrol et
        card = Card.objects.filter(user=user_id, product=product_id).first()
        print(card)
        if card:
            # Quantity 1'den büyükse bir azalt, eğer 1 ise sil
            if card.quantity > 1:
                
                card.quantity -= 1
                card.save()
            else:
                card.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

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

        print("alt taraf : ", instance.one_star)
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)    
        # self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)

# class DeleteRating(generics.DestroyAPIView):
#     queryset = Rate.objects.all()
#     serializer_class = RateSerializer
