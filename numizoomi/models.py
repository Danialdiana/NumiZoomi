from django.db import models
from django.urls import reverse


class Money(models.Model):
    title=models.CharField(max_length=255)
    description=models.TextField(blank=True)
    country = models.CharField(max_length=255)
    year = models.CharField(max_length=255)
    count = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    metal = models.CharField(max_length=255)
    time_create=models.DateTimeField(auto_now_add=True)
    time_update=models.DateTimeField(auto_now=True)
    is_published=models.BooleanField(default=True)
    image=models.ImageField(upload_to="photos/%Y/%m/%d/")
    category_id=models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
    )

    def ___str___(self):
        return self.title

    def get_absolute_url(self):
        return reverse('money', kwargs={'money_id':self.pk})

    class Meta:
        verbose_name_plural= 'Монеты'

class Category(models.Model):
    name = models.CharField(max_length=255)


    def ___str___(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id':self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
