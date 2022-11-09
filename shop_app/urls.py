from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from shop_app import views as user_views
from .views import *

urlpatterns = [
    path('',home, name='hom'),
    path('home/',home, name='home'),
    path('about/', about, name='about'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('contact/', contact, name='contact'),
    path('shop/', shop, name='shop'),
    path('shop-single/', shop_single, name='shop_single'),
    path('thankyou/', thankyou, name='thankyou'),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)