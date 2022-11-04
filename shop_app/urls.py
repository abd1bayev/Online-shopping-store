from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('home/',home),
    path('about/', about),
    path('cart/', cart),
    path('checkout/', checkout),
    path('contact/', contact),
    path('shop/', shop),
    path('shop-single/', shop_single),
    path('thankyou/', thankyou),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)