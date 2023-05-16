from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('cart/', views.cart, name="cart"),
    path('checkout/',views.checkout,name="checkout")
]