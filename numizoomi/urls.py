from django.urls import path

from.views import *

urlpatterns = [
    path('', index, name='home'),
    path('money/<int:money_id>/', show_money, name='money'),
    path('category/<int:cat_id>/', show_category, name='category'),
]

