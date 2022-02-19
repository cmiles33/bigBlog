from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST
from cart.forms import CartAddProductForm

from .models import CeramicCollection, Product

# Create your views here.


def main_ceramic_page(request):
    print("nothing yet")
    ceramic_categories = CeramicCollection.objects.all()

    return render(request, 'main_ceramic_page.html',
                  {"ceramic_post":ceramic_categories})


def catalog_view(request, collection_slug=None):
    print("Nothing")
    collection = None
    collections = CeramicCollection.objects.all()
    products = Product.objects.filter(available=True)
    if collection_slug:
        collection = get_object_or_404(CeramicCollection, slug=collection_slug)
        products = products.filter(category=collection)

    return render(request, 'catalog_page.html',
                  {'collection': collection,
                   'collections': collections,
                   'products': products})


def product_detail(request, id, product_slug):
    product = get_object_or_404(Product, id=id,
                                slug=product_slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,'product_detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
