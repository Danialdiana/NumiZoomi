from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse('Страница приложения')

def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageForbidden(request,exception):
    return HttpResponseNotFound('<h1>Вам запрещено!!! У вас нет доступа</h1>')

def pageBadRequest(request,exception):
    return HttpResponseNotFound('<h1>Запрос неверный</h1>')

def pageInternalServerError(request,exception):
    return HttpResponseNotFound('<h1>Внутреняя ошибка сервера</h1>')