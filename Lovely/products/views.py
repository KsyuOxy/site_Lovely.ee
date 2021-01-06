from django.shortcuts import render, redirect
from .models import Product
from django.http import Http404
from .forms import ProductForm


def products_list(request):
    data = dict()
    all_products = Product.objects.all()
    data['products'] = all_products
    print(data['products'])
    return render(request, 'products/products_list.html', context=data)


def update_product(request, product_id: int):
    data = dict()
    products = Product.objects.filter(id=product_id)
    if not request.user.is_superuser or not products.exists():
        raise Http404

    product = Product.objects.get(id=product_id)

    data['product'] = product
    print(data['product'])
    if request.method == 'GET':
        product_form = ProductForm(instance=product)
        data['product_form'] = product_form
        return render(request, 'products/update_product.html', context=data)
    elif request.method == 'POST':
        product_form = ProductForm(request.POST)
        if product_form.is_valid():
            product.name = product_form.cleaned_data['name']
            product.about = product_form.cleaned_data['about']
            product.expiration_date = product_form.cleaned_data['expiration_date']
            product.category = product_form.cleaned_data['category']
            product.save()
        else:
            print('NOT VALID FORM')
        return redirect('/products/products_list')


def delete_product(request, product_id: int):
    data = dict()
    products = Product.objects.filter(id=product_id)
    if not request.user.is_superuser or not products.exists():
        raise Http404

    product = Product.objects.get(id=product_id)

    if request.method == 'GET':
        data['product'] = product
        return render(request, 'products/delete_product.html', context=data)
    elif request.method == 'POST':
        product.delete()
        return redirect('/products/products_list')


def create_product(request):
    data = dict()
    if request.method == 'GET':
        product_form = ProductForm()
        data['product_form'] = product_form
        return render(request, 'products/create_product.html', context=data)
    elif request.method == 'POST':
        product_form = ProductForm(request.POST)
        product_form.save()
        return redirect('/products/products_list')


def product_details(request, product_id: int):
    product = Product.objects.get(id=product_id)
    data = dict()
    data['product'] = product
    return render(request, 'products/product_details.html', context=data)
