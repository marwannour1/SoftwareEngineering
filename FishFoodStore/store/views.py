from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    myproductname1 = Product.objects.get(id=1)
    myproductname2 = Product.objects.get(id=2)
    myproductname3 = Product.objects.get(id=3)
    myproductname4 = Product.objects.get(id=4)
    myproductname5 = Product.objects.get(id=5)
    myproductname6 = Product.objects.get(id=6)
    return render(request, "store/home.html", {
        "myproductname1" : myproductname1,
        "myproductname2" : myproductname2,
        "myproductname3" : myproductname3,
        "myproductname4" : myproductname4,
        "myproductname5" : myproductname5,
        "myproductname6" : myproductname6,
    })


def login(request):
    return render(request, "store/sign_in.html")

def signup(request):
    return render(request, "store/sign_up.html")

def cart(request):
    return render(request, "store/cartpro.html")

