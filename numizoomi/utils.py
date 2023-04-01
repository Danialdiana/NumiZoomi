import menu as menu
from django.db.models import Count

from numizoomi.models import Category


class DataMixin:
    paginate_by = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('money'))
        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context