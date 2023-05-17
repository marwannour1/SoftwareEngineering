from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Customer,Product,Order,OrderItem






def authenticate(email=None, password=None, **kwargs):
    try:
        customer = Customer.objects.get(email=email, password=password)
        return customer
    except Customer.DoesNotExist:
          return None

customer = None

# Create your views here.
def home(request):
    return render(request, "store/home.html")

def login(request):
    if request.method == "POST":
        loginemail = request.POST['email']
        loginpassword = request.POST['password']
        user = authenticate(email=loginemail, password=loginpassword)

        if user is not None:
            global customer
            customer = user
            
            return redirect('home')
        
        else:
            
            msg = "invalid email or password"
            return render(request, 'store/sign_in.html', {
                "msg": msg
            })
    return render(request, 'store/sign_in.html')


         




def signup(request):
    if request.method == 'POST':
        # Get the form data
        email = request.POST['email']
        password = request.POST['password']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        phone = request.POST['phone']
        district = request.POST['district']
        streetName = request.POST['streetName']
        buildingNumber = request.POST['buildingNumber']
        additionalInfo = request.POST['additionalInfo']

        if (email != '' and password != '' and firstName != '' and lastName != '' and phone != '' and district != '' and streetName != '' and buildingNumber != '' and additionalInfo != ''):



        # Create a new Customer object and save it to the database
            customer = Customer(email = email, password=password, firstName=firstName, lastName=lastName, phone=phone, district=district, 
                            streetName = streetName, buildingNumber = buildingNumber, additionalInfo = additionalInfo)
            customer.save()

        # Redirect to a success page
            return redirect('home')
        else:
            msg = "please fill in all the fields"
            return render(request, "store/sign_up.html", {
                "msg" : msg
                })

    # If the request method is GET, just show the signup form
    return render(request, 'store/sign_up.html')


def add_to_cart(request, product_id):
    
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = Product.objects.get(pk=product_id)
        customer.cart.add(product)
        return HttpResponse("Product added to cart.")

def cart(request):
    if customer != None:
        return render(request, "store/cartpro.html",{
            "products" : customer.cart
        })
    else:
        return redirect('login')

def checkout(request):
    if request.method=="POST":
        if customer != None:
            order = Order(customer=customer)
            order.save()
            for product in customer.cart.all():
                order_item = OrderItem(order=order, product=product)
                order_item.save()
        else:
            return redirect('login')
    return render(request, "store/checkout.html")





