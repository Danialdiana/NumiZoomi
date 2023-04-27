import menu as menu
from django.core.cache import cache

from django.db.models import Count

from numizoomi.models import Category


class DataMixin:
    paginate_by = 6

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = cache.get('category_id')
        if not cats:
            cats = Category.objects.annotate(Count('money'))
            cache.set('category_id', cats, 60)


        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context