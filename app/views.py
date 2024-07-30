from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, ProductEnter, Category


# Mahsulotlar ro'yxati
def home(request):
    productenters = ProductEnter.objects.all()
    context = {
        "products": productenters,
    }
    return render(request, "home.html", context)


def productenter_detail(request, generete_id):
    productenter = ProductEnter.objects.get(generete_id=generete_id)
    context = {
        "productenter": productenter,
    }
    return render(request, "create-update.html", context)


def create(request):
    if request.method == "POST":
        product_id = request.POST.get("product")
        name = request.POST["name"]
        description = request.POST["description"]
        price = request.POST["price"]
        quantity = request.POST["quantity"]
        if name and description and price:
            ProductEnter.objects.create(
                name=name,
                description=description,
                price=price,
                quantity=quantity,
                product_id=product_id,
            )
            return redirect("home")
    return render(request, "create-update.html")


def update(request, id):
    product = ProductEnter.objects.get(id=id)
    context = {
        "product": product,
    }
    if request.method == "POST":
        product.name = request.POST["name"]
        product.description = request.POST["description"]
        product.price = request.POST["price"]
        product.quantity = request.POST["quantity"]
        product.save()
        return redirect("home")
    return render(request, "create-update.html", context)


def delete(request, id):
    product = ProductEnter.objects.get(id=id)
    context = {
        "product": product,
    }
    if request.method == "POST":
        product.delete()
        return redirect("home")
    return render(request, "delete.html", context)
