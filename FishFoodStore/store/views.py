from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render,redirect
from .models import Customer, OrderItem, Product,Order

# Create your views here.
def home(request):
    return render(request, "store/home.html")

def login(request):
    return render(request, "store/sign_in.html")

def signup(request):
    return render(request, "store/sign_up.html")

def add_to_cart(request, product_id):
    customer = request.user.customer
    product = get_object_or_404(Product, pk=product_id)
    customer.cart.add(product)
    return HttpResponse("Product added to cart.")

def cart(request):
    customer = request.user.customer
    return render(request, "store/cartpro.html",{
        "products" : customer.cart
    })

def checkout(request):
    if request.method=="POST":
        if request.POST.get('customer'):
            customer_id = request.POST.get('customer')
            customer = Customer.objects.get(pk=customer_id)
            order = Order(customer=customer)
            order.save()
            for product in customer.cart.all():
                order_item = OrderItem(order=order, product=product)
                order_item.save()
        else:
            return redirect('login')
    return render(request, "store/checkout.html")

    