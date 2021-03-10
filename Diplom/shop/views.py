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
