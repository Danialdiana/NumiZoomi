from django import forms
from django.core.exceptions import ValidationError
from django.utils.functional import empty

from .models import *

class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category_id'].empty_label = "Категория не выбрана"

    class Meta:
        model = Money
        fields = ['title', 'slug', 'description', 'country', 'year', 'count', 'price', 'metal', 'image', 'is_published', 'category_id']
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