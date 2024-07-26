from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, ProductEnter, Category


# Mahsulotlar ro'yxati
def home(request):
    products = Product.objects.all()
    context = {
        "products": products,
    }
    return render(request, "home.html", context)


def create(request):
    if request.method == "POST":
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]
        # category = request.POST["category_name"]
        quantity = request.POST["quantity"]
        if name and description and price:
            Product.objects.create(
                name=name,
                description=description,
                price=price,
                # category=category,
                quantity=quantity,
            )
            return redirect("home")
    return render(request, "create-update.html")


def update(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product,
    }
    if request.method == "POST":
        product.name = request.POST["name"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]
        product.category = request.POST["category"]
        product.quantity = request.POST["quantity"]
        product.save()
        return redirect("home")
    return render(request, "create-update.html", context)


def delete(request, id):
    product = Product.objects.get(id=id)
    context = {
        "product": product,
    }
    if request.method == "POST":
        product.delete()
        return redirect("home")
    return render(request, "delete.html", context)
