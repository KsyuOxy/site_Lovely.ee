from django.shortcuts import render, HttpResponse


# Create your views here.
def index(request):
    return render(request, 'base.html')  # request, путь к файлу который хотим отобразить на странице
    # return HttpResponse('Hello')


def html_main_page(request):
    return render(request, 'home/html-main_page.html')


def multipage(request, page_id: int):
    data = {
        'page__id': page_id
    }
    return render(request, 'home/multi-value-page.html', context=data)


def sign_in(request):
    return render(request, 'home/login.html')


def register(request):
    return render(request, 'home/register.html')


def catalog(request):
    return render(request, 'home/catalog.html')


def delivery(request):
    return render(request, 'home/delivery.html')


def contacts(request):
    return render(request, 'home/contacts.html')


def reviews(request):
    return render(request, 'home/reviews.html')


def promotion(request):
    return render(request, 'home/promotion.html')
