from django.db import models
from django.urls import reverse


class Money(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    description = models.TextField(blank=True, verbose_name="Описание")
    country = models.CharField(max_length=255, verbose_name="Производства")
    year = models.CharField(max_length=255, verbose_name="Год")
    count = models.CharField(max_length=255, verbose_name="Количество")
    price = models.CharField(max_length=255, verbose_name="Цена")
    metal = models.CharField(max_length=255, verbose_name="Металл")
    time_create=models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update=models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    is_published=models.BooleanField(default=True, verbose_name="Публикация")
    image=models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    category_id=models.ForeignKey(
        'Category',
        on_delete=models.PROTECT, verbose_name="Категории"
    )

    def ___str___(self):
        return self.title

    def get_absolute_url(self):
        return reverse('money', kwargs={'money_slug':self.slug})

    class Meta:
        verbose_name_plural= 'Монеты'
        ordering = ['-time_create', 'title']

class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Категория")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    def ___str___(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'category_id':self.pk})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']
