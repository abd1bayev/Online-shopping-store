from django.urls import path
from .views import *

urlpatterns = [
    path('home/',home),
    path('about/', about),
    path('cart/', cart),
    path('checkout/', checkout),
    path('contact/', contact),
    path('shop/', shop),
    path('shop_single/', shop_single),
    path('thankyou/', thankyou),
]