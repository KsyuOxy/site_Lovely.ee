from django.shortcuts import render, redirect
from .models import Categories
from .forms import CategoryForm


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
    return render(request, 'categories/delete.html')


def update_category(request, category_id: int):
    return render(request, 'categories/update.html')


def category_details(request, category_id: int):
    return render(request, 'categories/details.html')


def category_list(request):
    data = dict()
    all_categories = Categories.objects.all()

    data['categories'] = all_categories
    return render(request, 'categories/category_list.html', context=data)
