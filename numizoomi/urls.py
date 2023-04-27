from django.urls import path

from.views import *

urlpatterns = [
    path('', MoneyHome.as_view(), name='home'),
    path('admin/', admin, name='admin'),
    path('addpage/', AddMoney.as_view(), name='add_money'),
    path('money/<slug:money_slug>/', ShowPost.as_view(), name='money'),
    path('category/<int:category_id>/', MoneyCategory.as_view(), name='category'),
    path('login/', LoginUser.as_view(), name='logiin'),
    path('logout/', logout_user, name='logoutt'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('contact/', ContactFormView.as_view(), name='contact'),
]

