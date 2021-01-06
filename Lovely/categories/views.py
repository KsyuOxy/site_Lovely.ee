from django.shortcuts import render, redirect
from .models import Categories
from products.models import Product
from .forms import CategoryForm
from django.http import Http404


# Create your views here.
def index(request):
    data = dict()
    all_categories = Categories.objects.all()

    data['categories'] = all_categories
    return render(request, 'categories/index.html', context=data)


def create_category(request):
    data = dict()
    if request.method == 'GET':
        category_form = CategoryForm()
        data['category_form'] = category_form
        return render(request, 'categories/create.html', context=data)
    elif request.method == 'POST':
        category_form = CategoryForm(request.POST)
        category_form.save()
        return redirect('/categories/list')


def delete_category(request, category_id: int):
    data = dict()
    categories = Categories.objects.filter(id=category_id)
    if not request.user.is_superuser or not categories.exists():
        raise Http404

    category = Categories.objects.get(id=category_id)

    if request.method == 'GET':
        data['category'] = category
        return render(request, 'categories/delete.html', context=data)
    elif request.method == 'POST':
        category.delete()
        return redirect('/categories/list')


def update_category(request, category_id: int):
    data = dict()
    categories = Categories.objects.filter(id=category_id)
    if not request.user.is_superuser or not categories.exists():
        raise Http404

    category = Categories.objects.get(id=category_id)

    data['category'] = category
    print(data['category'])
    if request.method == 'GET':
        category_form = CategoryForm(instance=category)
        data['category_form'] = category_form
        return render(request, 'categories/update.html', context=data)
    elif request.method == 'POST':
        category_form = CategoryForm(request.POST)
        if category_form.is_valid():
            category.name = category_form.cleaned_data['name']
            category.about = '(EDITED)' + category_form.cleaned_data['about']
            category.max_products = category_form.cleaned_data['max_products']
            category.in_stock = category_form.cleaned_data['in_stock']
            category.save()
        else:
            print('NOT VALID FORM')
        return redirect('/categories/list')


def category_details(request, category_id: int):
    data = dict()
    categories = Categories.objects.filter(id=category_id)
    if not categories.exists():
        raise Http404
    category = Categories.objects.get(id=category_id)
    products = Product.objects.filter(category__name=category.name)
    data['category'] = category
    data['products'] = products
    return render(request, 'categories/details.html', context=data)


def category_list(request):
    data = dict()
    all_categories = Categories.objects.all()
    data['categories'] = all_categories
    return render(request, 'categories/category_list.html', context=data)
