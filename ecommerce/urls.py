from rest_framework import routers
from django.urls import path
from .views import ProductViewSet, CardViewSet, BrandViewSet, RateUpdateView, DeleteRating

router = routers.DefaultRouter()
router.register("products", ProductViewSet)
router.register("brands", BrandViewSet)
# router.register("rate", RateViewSet)

urlpatterns = [
    # path('/', )
    path('rate/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('ratedelete/<int:pk>/', DeleteRating.as_view(), name='rate-delete'),
]
urlpatterns += router.urls