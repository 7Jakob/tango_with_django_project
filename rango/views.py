from django.shortcuts import render
from rango.models import Category, Page


def encode_url(name):
    return name.replace(' ', '_')


def decode_url(name):
    return name.replace('_', ' ')


def index(request):
    category_list = Category.objects.all()

    context_dict = {
        'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!',
        'categories': category_list,
    }

    return render(request, 'rango/index.html', context=context_dict)


def show_category(request, category_name_slug):
    category_name = decode_url(category_name_slug)
    context_dict = {}

    try:
        category = Category.objects.get(name=category_name)
        pages = Page.objects.filter(category=category)

        context_dict['category'] = category
        context_dict['pages'] = pages

    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)



def about(request):
    return render(request, 'rango/about.html')
