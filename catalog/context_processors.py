from .cart import Cart

def cart(request):
    return {'cart': Cart(request)}
def categories(request):
    from .models import Category
    return {'categories': Category.objects.all()}