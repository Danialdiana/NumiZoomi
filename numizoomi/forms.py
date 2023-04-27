from captcha.fields import CaptchaField
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.utils.functional import empty

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_id'].empty_label = "Категория не выбрана"

    class Meta:
        model = Money
        fields = ['title', 'slug', 'description', 'country', 'year', 'count', 'price', 'metal', 'image', 'is_published', 'category_id','user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'cols': 100, 'rows': 8}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.TextInput(attrs={'class': 'form-control'}),
            'count': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.TextInput(attrs={'class': 'form-control'}),
            'metal': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

    def clean_count(self):
        count = self.cleaned_data['count']
        if empty(count):
            raise ValidationError('Напишите количество монет')

        return count

    def clean_price(self):
        price = self.cleaned_data['price']
        if empty(price):
            raise ValidationError('Напишите стоимость монет')

        return price

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255,widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(label='Сообщения',widget=forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'form-control'}))
    capatcha = CaptchaField()
