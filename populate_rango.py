import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page


def add_page(cat, title, url, views=0):
    page, created = Page.objects.get_or_create(category=cat, title=title)
    page.url = url
    page.views = views
    page.save()
    return page


def add_cat(name, views=0, likes=0):
    cat, created = Category.objects.get_or_create(name=name)
    cat.views = views
    cat.likes = likes
    cat.save()
    return cat


def populate():
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'https://docs.python.org/3/tutorial/', 'views': 128},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/', 'views': 64},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/', 'views': 32},
    ]

    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.2/intro/tutorial01/', 'views': 128},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/', 'views': 64},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/', 'views': 32},
    ]

    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/', 'views': 128},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org', 'views': 64},
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16},
    }

    for cat_name, cat_data in cats.items():
        c = add_cat(cat_name, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f"- {c}: {p}")


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
