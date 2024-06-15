# from django.db.models import Q
from django.shortcuts import render

from ice_cream.models import IceCream


# def index(request):
#     template = 'homepage/index.html'
#     ice_cream_list = IceCream.objects.values(
#         'id', 'title', 'description'
#     ).filter(
#         Q(is_on_main=True) & Q(is_published=True)
#         | Q(is_published=True) & Q(title__contains='пломбир')
#     ).order_by(
#         'title'
#     )[:4]
#     context = {
#         'ice_cream_list': ice_cream_list,
#     }
#     return render(request, template, context)

# homepage/views.py

def index(request):
    template = 'homepage/index.html'
    # Запрашиваем нужные поля из базы данных:
    ice_cream_list = IceCream.objects.values(
        'id', 'title', 'price', 'description'
    ).filter(
        # Проверяем, что
        is_published=True,  # Сорт разрешён к публикации;
        is_on_main=True,  # Сорт разрешён к публикации на главной странице;
        category__is_published=True  # Категория разрешена к публикации.
    )

    context = {
        'ice_cream_list': ice_cream_list,
    }
    return render(request, template, context)
