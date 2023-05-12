from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "store/home.html")

def login(request):
    return render(request, "store/sign_in.html")

def signup(request):
    return render(request, "store/sign_up.html")

def cart(request):
    return render(request, "store/cartpro.html")

