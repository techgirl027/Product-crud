from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product


# Mahsulotlar ro'yxati
def product_list(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "home.html", context)


# Mahsulot qo'shish
def product_create(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]
        category = request.POST["category"]
        quantity = request.POST["quantity", 1]
        if name and description and price and category:
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                category=category,
                quantity=quantity,
            )
            return redirect("product_list")
    return render(request, "create-update.html")


# Mahsulotni tahrirlash
def product_update(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product,
    }
    if request.method == "POST":
        product.name = request.POST["name"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]
        product.category = request.POST["category"]
        product.quantity = request.POST["quantity", 1]
        product.save()
        return redirect("product_list")
    return render(request, "create-update.html", context)


# Mahsulotni o'chirish
def product_delete(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product,
    }
    if request.method == "POST":
        product.delete()
        return redirect("product_list")
    return render(request, "delete.html", context)
