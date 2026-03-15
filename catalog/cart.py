from .models import Product
import copy
class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_cart')
        
        if not cart:
            cart = self.session['session_cart'] = {}
        
        self.cart = cart
    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'price': str(product.price), 'quantity': 1}
        else:
            self.cart[product_id]['quantity'] += 1
        self.session.modified = True
    def delete(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True
    def update(self, product_id, quantity):
        product_id = str(product_id)
        if product_id in self.cart:
            self.cart[product_id]['quantity'] = int(quantity)
            self.session.modified = True
    def clear(self):
        self.session['session_cart'] = {}
        self.session.modified = True
    def __len__(self):
        return sum(item['quantity'] for item in self.cart.values())
    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        
        import copy
        cart_copy = copy.deepcopy(self.cart)
        for product in products:
            product_id = str(product.id)
            if product_id in cart_copy:
                cart_copy[product_id]['product'] = product
        for item in cart_copy.values():
            if 'product' not in item:
                continue
            item['price'] = float(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def get_total_price(self):
        return sum(float(item['price']) * item['quantity'] for item in self.cart.values())