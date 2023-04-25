from django.contrib.auth import login, logout
from django.contrib.auth.views import LoginView
from django.forms import model_to_dict
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseForbidden, HttpResponseBadRequest, \
    HttpResponseServerError, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, FormView
from rest_framework import generics, viewsets, mixins
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet

from .forms import *
from .models import *
from .permissions import IsOwnerOrReadOnly, IsAdminOrReadOnly
from .serializers import MoneySerializer
from .utils import DataMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class MoneyHome(DataMixin, ListView):

    model = Money
    template_name = 'numizoomi/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title = 'Главная страница')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Money.objects.filter(is_published=True).select_related('category_id')

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

class ShowPost(DataMixin, DetailView):
    model = Money
    template_name = 'numizoomi/money.html'
    slug_url_kwarg = 'money_slug'
    context_object_name = 'money'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['money'])
        return dict(list(context.items()) + list(c_def.items()))

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

class MoneyCategory(DataMixin, ListView):
    model = Money
    template_name = 'numizoomi/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Money.objects.filter(category_id=self.kwargs['category_id'], is_published=True).select_related('category_id')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c = Category.objects.get(id=self.kwargs['category_id'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


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

class AddMoney(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'numizoomi/addmoney.html'
    success_url = reverse_lazy('home')
    login_url = '/admin/'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить монет')
        return dict(list(context.items()) + list(c_def.items()))

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

class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'numizoomi/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'numizoomi/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'numizoomi/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home')


class MoneyViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = MoneySerializer

    def get_queryset(self):
        pk = self.kwargs.get("pk")

        if not pk:
            return Money.objects.all()[:3]

        return Money.objescts.filter(pk=pk)

    @action(method=['get'], detail=False)
    def category(self, request, pk=None):
        cats = Category.objects.get(pk=pk)
        return Response({'cats': cats.name})

class MoneyAPIListPagination(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000

class MoneyAPIList(generics.ListCreateAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer


class MoneyAPIUpdate(generics.UpdateAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
    permission_classes = (IsOwnerOrReadOnly,)


class MoneyAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
    permission_classes = (IsAdminOrReadOnly,)


# class MoneyAPIView(APIView):
#     def get(self, request):
#         w = Money.objects.all()
#         return Response({'moneys': MoneySerializer(w, many=True).data})
#
#     def post(self, request):
#         serializer = MoneySerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'money': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#
#         try:
#             instance = Money.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exists"})
#
#         serializer = MoneySerializer(data=request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"money": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#
#         return Response({"post": "delete money " + str(pk)})


class MoneyAPIView(generics.ListAPIView):
    queryset = Money.objects.all()
    serializer_class = MoneySerializer
