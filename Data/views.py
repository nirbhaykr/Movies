from django.shortcuts import render
from django.views.generic.list import ListView
from Data.models import Movies, Category
import ipdb

# Create your views here.

class MoviesListhView(ListView):
    """
    MoviesListhView
    """
    template_name = 'movies_list.html'
    model = Movies
    paginate_by = 10

    def get_context_date(self, **kwargs):
        context = super(MoviesListhView, self).get_context_data(csrfproctection=True, **kwargs)
        return context

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
            
        self.object_list = queryset
        context = self.get_context_data(**kwargs)
        context['category'] = Category.objects.filter(type__iexact="Language")
        context['genre'] = Category.objects.filter(type__iexact="Genre")
        context['selected_category'] = request.GET.get('category',None)
        context['selected_genre'] = request.GET.get('genre',None)
        context['selected_order'] = request.GET.get('sort_by',None)
        
        query_items = request.GET.copy()
        if query_items.has_key('page'):
            del query_items['page']
        
        context['query_items'] = query_items 
        
        return self.render_to_response(context)
    
    def get_queryset(self):
        """
        Return the list of items for this view.
 
        The return value must be an iterable and may be an instance of
        `QuerySet` in which case `QuerySet` specific behavior will be enabled.
        """
        request = self.request
        queryset = Movies.objects.all()
        cat_list = []
        
        if request.GET.get('category',None):
            cat_list.extend(Category.objects.filter(id = request.GET.get('category',None)))
            
        if request.GET.get('genre',None):
            cat_list.extend(Category.objects.filter(id = request.GET.get('genre',None)))
        
        if cat_list:
            queryset = queryset.filter(category__in = cat_list)
            
        if request.GET.get('sort_by',None):
            queryset = queryset.order_by(request.GET.get('sort_by',None))
        return queryset