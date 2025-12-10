# product/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, ProductImage, Productmetainformation
from django.urls import reverse
from django.http import HttpResponseRedirect

def product_list(request):
    products = Product.objects.all().order_by("-created_at")
    return render(request, "product/product_list.html", {"products": products})

def product_detail(request, slug):
    product = get_object_or_404(Product, product_slug=slug)
    try:
        meta = product.productmetainformation
    except Productmetainformation.DoesNotExist:
        meta = None
    images = product.image.all()
    return render(request, "product/product_detail.html", {"product": product, "meta": meta, "images": images})

# Simple session cart:
def add_to_cart(request, slug):
    product = get_object_or_404(Product, product_slug=slug)
    cart = request.session.get("cart", {})
    # key by product uid (string)
    key = str(product.uid)
    cart[key] = cart.get(key, {"qty": 0, "name": product.Product_name, "price": product.product_price})
    cart[key]["qty"] += 1
    request.session["cart"] = cart
    request.session.modified = True
    return redirect("product:cart_view")

def cart_view(request):
    cart = request.session.get("cart", {})
    items = []
    total = 0
    for pid, data in cart.items():
        line_total = data["qty"] * data["price"]
        items.append({"uid": pid, "name": data["name"], "qty": data["qty"], "price": data["price"], "line_total": line_total})
        total += line_total
    return render(request, "product/cart.html", {"items": items, "total": total})

def remove_from_cart(request, uid):
    cart = request.session.get("cart", {})
    if uid in cart:
        del cart[uid]
        request.session["cart"] = cart
        request.session.modified = True
    return redirect("product:cart_view")
