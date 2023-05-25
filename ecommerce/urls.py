from rest_framework import routers
from django.urls import path
from .views import ProductViewSet, BrandViewSet, RateUpdateView, CreateCardProductViewSet, DeleteCardProductViewSet

router = routers.DefaultRouter()
router.register("products", ProductViewSet)
router.register("brands", BrandViewSet)


urlpatterns = [
    # path('/', )
    path('rate/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('create-card-product/', CreateCardProductViewSet.as_view({'post': 'create'}), name='create-card-product'),
    path('delete-card-product/', DeleteCardProductViewSet.as_view({'post': 'delete_card_product'}), name='delete-card-product'),

]
urlpatterns += router.urls