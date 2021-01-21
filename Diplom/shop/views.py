from django.shortcuts import render
from .models import Category, Product
from django.db.models import Q
from django.views.generic import DetailView


def home(request):
    return render(request, 'shop/home.html')


def glasses(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) or Q(
            category__icontains=search_query))
    else:
        products = Product.objects.all()

    return render(request, 'shop/glasses.html',
                  context={'products': products})


def sun_glasses(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) or Q(
            category__icontains=search_query))
    else:
        products = Product.objects.filter(type='Sun')

    return render(request, 'shop/sun_glasses.html',
                  context={'products': products})


def sun_mens_glasses(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) or Q(
            category__icontains=search_query))
    else:
        products = Product.objects.filter(type='Sun', category=1)

    return render(request, 'shop/sun_glasses.html',
                  context={'products': products})


def sun_womens_glasses(request):
    search_query = request.GET.get('search', '')
    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) or Q(
            category__icontains=search_query))
    else:
        products = Product.objects.filter(type='Sun', category=2)

    return render(request, 'shop/sun_glasses.html',
                  context={'products': products})


def optical_glasses(request):
    search_query = request.GET.get('search', '')

    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) or Q(
            category__icontains=search_query))
    else:
        products = Product.objects.filter(type='Optical')

    return render(request, 'shop/optical_glasses.html',
                  context={'products': products})


def optical_mens_glasses(request):
    search_query = request.GET.get('search', '')

    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) or Q(
            category__icontains=search_query))
    else:
        products = Product.objects.filter(type='Optical', category=1)

    return render(request, 'shop/optical_glasses.html',
                  context={'products': products})


def optical_womens_glasses(request):
    search_query = request.GET.get('search', '')

    if search_query:
        products = Product.objects.filter(Q(name__icontains=search_query) or Q(
            category__icontains=search_query))
    else:
        products = Product.objects.filter(type='Optical', category=2)

    return render(request, 'shop/optical_glasses.html',
                  context={'products': products})


class ProductDetailView(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context
