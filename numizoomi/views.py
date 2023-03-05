from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseServerError, Http404
from django.shortcuts import render


from .models import *


# Create your views here.
def index(request):
    moneys = Money.objects.all()

    context = {
        'posts': moneys,
        'title': 'Главная страница',
        'cat_selected': 0,
    }

    return render(request, 'numizoomi/index.html', context=context)

def show_money(request, money_id):
    return HttpResponse(f"Отображение монеты с id = {money_id}")

def show_category(request, cat_id):
    posts = Money.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    context = {
        'posts': posts,
        'title': 'Отображение по рубрикам',
        'cat_selected': cat_id,
    }

    return render(request, 'numizoomi/index.html', context=context)


def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageForbidden(request,exception):
    return HttpResponseForbidden('<h1>Вам запрещено!!! У вас нет доступа</h1>')

def pageBadRequest(request,exception):
    return HttpResponseBadRequest('<h1>Запрос неверный</h1>')

def pageInternalServerError(request):
    return HttpResponseServerError('<h1>Внутреняя ошибка сервера</h1>')