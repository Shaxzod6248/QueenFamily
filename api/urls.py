from django.conf import settings
from django.urls import path, include
from .views import *
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register('Category', CategoryViewSet)
router.register('Products', ProductsViewSet)
router.register('Orders', OrdersViewSet)
router.register('Order_details', Order_detailViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]