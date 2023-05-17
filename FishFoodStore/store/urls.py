from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),
    path('add_to_cart/<int:product_id>/',views.add_to_cart,name="addToCart"),
    path('home/cart/', views.cart, name="cart"),

]