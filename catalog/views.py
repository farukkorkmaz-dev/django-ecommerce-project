from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import Product
from .cart import Cart
from django.contrib import messages
from .forms import OrderCreateForm
from .models import OrderItem
def product_list(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(name__icontains=query)
    category_id = request.GET.get('category')
    if category_id:
        products = products.filter(category_id=category_id)
    sort_by = request.GET.get('sort')
    if sort_by == 'price_asc':
        products = products.order_by('price') 
    elif sort_by == 'price_desc':
        products = products.order_by('-price') 
    elif sort_by == 'newest':
        products = products.order_by('-id') 
    else:
        products = products.order_by('-id')

    return render(request, 'catalog/index.html', {'products': products})
   
        
    return render(request, 'catalog/index.html', {'products': products})
   
def product_detail(request, pk): 
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/detail.html', {'product': product})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'catalog/register.html', {'form': form})

def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('index')
def cart_delete(request, product_id):
    cart = Cart(request)
    cart.delete(product_id=product_id) 
    return redirect('cart_summary')
def cart_update(request):
    if request.method == 'POST':
        cart = Cart(request)
        product_id = request.POST.get('product_id')
        quantity = request.POST.get('quantity')
        cart.update(product_id=product_id, quantity=quantity)
    return redirect('cart_summary')
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_summary')

def cart_summary(request):
    cart = Cart(request)
    return render(request, 'catalog/cart_summary.html', {'cart': cart})
def order_create(request):
    cart = Cart(request) 
    if len(cart) == 0:
        messages.error(request, "Sepetiniz boş, sipariş oluşturamazsınız.")
        return redirect('index')

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()   
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear() 
            return render(request, 'catalog/order_created.html', {'order': order})
    else:
        if request.user.is_authenticated:
            form = OrderCreateForm(initial={
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
            })
        else:
            form = OrderCreateForm()

    return render(request, 'catalog/order_create.html', {'form': form, 'cart': cart})

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()   
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear() 
            return render(request, 'catalog/order_created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'catalog/order_create.html', {'form': form, 'cart': cart})
