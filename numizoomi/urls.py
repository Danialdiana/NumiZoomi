from django.urls import path

from.views import *

urlpatterns = [
    path('', MoneyHome.as_view(), name='home'),
    path('addpage/', AddMoney.as_view(), name='add_money'),
    path('money/<slug:money_slug>/', ShowPost.as_view(), name='money'),
    path('category/<int:category_id>/', MoneyCategory.as_view(), name='category'),

]

