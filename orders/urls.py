# orders/urls.py

from django.urls import path
from .views import BuyOrderAPIView

urlpatterns = [
    path('buy/', BuyOrderAPIView.as_view(), name='buy-order')
]
