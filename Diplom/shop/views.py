from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.db.models import Q
from django.views.generic import ListView
from cart.forms import CartAddProductForm


class GlassesView(ListView):
    model = Product
    template_name = 'shop/glasses.html'
    context_object_name = 'products'

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search', '')
        if search:
            products = Product.objects.filter(
                Q(name__icontains=search) or Q(
                    category__icontains=search))
            return render(request, 'shop/glasses.html',
                          context={'products': products})
        else:
            products = Product.objects.all()
            if kwargs != {}:
                if len(kwargs) == 2:
                    product_category = kwargs['category']
                    product_type = kwargs['type'].title()
                    products = Product.objects.filter(type=product_type,
                                                      category=product_category)
                    return render(request, 'shop/glasses.html',
                                  context={'products': products})
                else:
                    product_type = kwargs['type'].title()
                    products = Product.objects.filter(type=product_type)
                    return render(request, 'shop/glasses.html',
                                  context={'products': products})
            else:
                return render(request, 'shop/glasses.html',
                              context={'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/product_detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})


"""Наброски пагинации"""
"""
paginator = Paginator(products, 6)
        page_number = request.GET.get('page', 1)
        page = paginator.get_page(page_number)
        is_paginator = page.has_other_pages()
        if page.has_previous():
            prev_url = '?page={}'.format(page.previous_page_number())
        else:
            prev_url = ''

        if page.has_next():
            next_url = '?page={}'.format(page.next_page_number())
        else:
            next_url = ''

        context = {
            'page_object': page,
            'is_paginated': is_paginator,
            'next_url': next_url,
            'prev_url': prev_url,
            'products': products,
        }
"""