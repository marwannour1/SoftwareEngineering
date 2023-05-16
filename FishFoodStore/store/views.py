from django.shortcuts import render,redirect
from .models import Customer, Product,Order

# Create your views here.
def home(request):
    return render(request, "store/home.html")

def login(request):
    return render(request, "store/sign_in.html")

def signup(request):
    return render(request, "store/sign_up.html")

def cart(request,product_id):
    product=Product.objects.get(id=product_id)
    return render(request, "store/cartpro.html",{
        "product" : product
    })

def checkout(request):
    return render(request, "store/checkout.html")

    