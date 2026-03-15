from django.contrib import admin
from .models import Category, Product
from django.contrib import admin
from .models import Order, OrderItem
admin.site.register(Category)
admin.site.register(Product)
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'address', 'city', 'paid', 'created_at']
    list_filter = ['paid', 'created_at']
    inlines = [OrderItemInline]
