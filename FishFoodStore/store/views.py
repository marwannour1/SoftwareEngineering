from django.shortcuts import render,redirect
from django.http import JsonResponse
from FishFoodStore.store.models import Product,Order

# Create your views here.
def home(request):
    return render(request, "store/home.html")

def login(request):
    return render(request, "store/sign_in.html")

def signup(request):
    return render(request, "store/sign_up.html")

def cart(request):
    return render(request, "store/cartpro.html")
def checkout(request):
    if request.method == 'POST':
        # Get the customer's details from the server-side session or database
        if request.user.is_authenticated:
            customer = request.user.customer
        else:
            # Handle error case if customer is not logged in
            return JsonResponse({'error': 'Customer not logged in'})
        
        cart = request.POST.get('cart')
        
        # Create an order for each item in the cart
        for item in cart['items']:
            product = Product.objects.get(pk=item['id'])
            order = Order(customer=customer, product=product, quantity=item['quantity'], line_price=item['line_price'])
            order.save()
        
        # Return a JSON response with the new order ID
        return JsonResponse({'order_id': order.pk})
    else:
        return redirect('cart')


    