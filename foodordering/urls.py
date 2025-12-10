"""
URL configuration for foodordering project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from . import views 
app_name  = "product"
urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.product_list, name="product_list"),
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),
    path("cart/add/<slug:slug>/", views.add_to_cart, name="add_to_cart"),
    path("cart/", views.cart_view, name="cart_view"),
    path("cart/remove/<str:uid>/", views.remove_from_cart, name="remove_from_cart"),
    path('', include('product.urls', namespace='product')),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)