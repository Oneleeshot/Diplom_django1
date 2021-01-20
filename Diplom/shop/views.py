from django.shortcuts import render
from .models import Category, Product
from django.db.models import Q
from django.views.generic import DetailView


def home(request):
    return render(request, 'shop/home.html')


def sun_glasses(request):
    search_query = request.GET.get('search', '')

    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) or Q(
            category__icontains=search_query))
    else:
        products = Product.objects.all()

    return render(request, 'shop/sun_glasses.html',
                  context={'products': products})


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
