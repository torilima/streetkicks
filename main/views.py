from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product

def show_main(request):
    product_list = Product.objects.all()

    context = {
        'npm' : '2406496391',
        'name': 'StreetKicks',
        'name': 'Abelyvia Tori Rebecca Silalahi',
        'class': 'PBP F',
        'product_list' : product_list
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.increment_views()

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)
