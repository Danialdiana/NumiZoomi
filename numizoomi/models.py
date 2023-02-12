from django.db import models

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

class Category(models.Model):
    name = models.CharField(max_length=255)
    money_id = models.ForeignKey(
        'Money',
        on_delete=models.CASCADE,
    )