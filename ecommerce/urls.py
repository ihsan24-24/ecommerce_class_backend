from rest_framework import routers
from django.urls import path
from .views import ProductViewSet, BrandViewSet, RateUpdateView, CardCreateView, CardDeleteView

router = routers.DefaultRouter()
router.register("products", ProductViewSet)
router.register("brands", BrandViewSet)


urlpatterns = [
    # path('/', )
    path('rate/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('card/delete/', CardDeleteView.as_view(), name='card-delete'),
    path('card/create/', CardCreateView.as_view(), name='card-create')
    # path('ratedelete/<int:pk>/', DeleteRating.as_view(), name='rate-delete'),
]
urlpatterns += router.urls