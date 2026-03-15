"""
URL configuration for my_shop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from catalog.views import product_list, product_detail, register, cart_add, cart_summary, cart_delete, cart_update, cart_clear, order_create
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='index'),
    path('register/', register, name='register'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('login/', auth_views.LoginView.as_view(template_name='catalog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='index'), name='logout'),
    path('cart/add/<int:product_id>/', cart_add, name='cart_add'),
    path('cart/', cart_summary, name='cart_summary'),
    path('cart/delete/<int:product_id>/', cart_delete, name='cart_delete'),
    path('cart/update/', cart_update, name='cart_update'),
    path('cart/clear/', cart_clear, name='cart_clear'),
    path('order/create/', order_create, name='order_create'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    