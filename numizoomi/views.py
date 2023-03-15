from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseServerError, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView

from .forms import AddPostForm
from .models import *


# Create your views here.

class MoneyHome(ListView):
    model = Money
    template_name = 'numizoomi/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Money.objects.filter(is_published=True)

# def index(request):
#     moneys = Money.objects.all()
#
#     context = {
#         'posts': moneys,
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'numizoomi/index.html', context=context)

class ShowPost(DetailView):
    model = Money
    template_name = 'numizoomi/money.html'
    slug_url_kwarg = 'money_slug'
    context_object_name = 'money'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['money']
        return context

# def show_money(request, money_slug):
#     money = get_object_or_404(Money, slug=money_slug)
#
#     context = {
#         'post': money,
#         'title': money.title,
#         'cat_selected': money.category_id,
#     }
#
#     return render(request, 'numizoomi/money.html', context=context)

    # return HttpResponse(f"Отображение монеты с id = {money_id}")

class MoneyCategory(ListView):
    model = Money
    template_name = 'numizoomi/index.html'
    context_object_name = 'moneys'
    allow_empty = False

    def get_queryset(self):
        return Money.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['moneys'][0].category_id)
        context['category_selected'] = context['moneys'][0].category_id
        return context


# def show_category(request, cat_id):
#     posts = Money.objects.filter(slug=cat_id)
#
#     if len(posts) == 0:
#         raise Http404()
#
#     context = {
#         'posts': posts,
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'numizoomi/index.html', context=context)

class AddMoney(CreateView):
    form_class = AddPostForm
    template_name = 'numizoomi/addmoney.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавить монет'
        return context

# def addmoney(request):
#     if request.method == 'POST':
#         form = AddPostForm(request.POST, request.FILES)
#         if form.is_valid():
#             #print(form.cleaned_data)
#             form.save()
#             return redirect('home')
#     else:
#         form = AddPostForm()
#     return render(request, 'numizoomi/addmoney.html', {'form': form, 'title': 'Добавить монеты'})
def pageNotFound(request,exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')

def pageForbidden(request,exception):
    return HttpResponseForbidden('<h1>Вам запрещено!!! У вас нет доступа</h1>')

def pageBadRequest(request,exception):
    return HttpResponseBadRequest('<h1>Запрос неверный</h1>')

def pageInternalServerError(request):
    return HttpResponseServerError('<h1>Внутреняя ошибка сервера</h1>')