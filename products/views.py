from django.shortcuts import render

from django.http import JsonResponse

from .models import Product, Manufacturer

def product_list(request):
    products = Product.objects.all()#[:30]
    data = {'products': list(products.values())}#'pk', 'name'
    response = JsonResponse(data)
    return response

def product_detail(request, pk):
    try:
        product = Product.objects.get(pk=pk)
        data = {'product': {
            'name': product.name,
            'Manufacturer': product.manufacturer.name,
            'Quantity': product.quantity,
            'Description': product.description,
            'Photo': product.photo.url,
            'Price': product.price,
            'Shipping cost': product.shipping_cost
        }}
        response = JsonResponse(data)
    except Product.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'Product not found'
            }
        },
        status=404)

    return response


def manufacturer_list(request):
    manufacturers = Manufacturer.objects.filter(active=True)
    data = {'manufacturers': list(manufacturers.values())}#'pk', 'name'
    response = JsonResponse(data)
    return response


def manufacturer_detail(request, pk):
    try:
        manufacturers = Manufacturer.objects.get(pk=pk)
        manufacturer_product = manufacturers.products.all()
        data = {'manufacturers': {
            'name': manufacturers.name,
            'location': manufacturers.location,
            'active': manufacturers.active,
            'products': list(manufacturers.products.values())

        }}
        response = JsonResponse(data)
    except Manufacturer.DoesNotExist:
        response = JsonResponse({
            'error': {
                'code': 404,
                'message': 'manufacturers not found'
            }
        },
        status=404)

    return response



# from django.views.generic.detail import DetailView
# from django.views.generic.list import ListView
#
#
#
# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'
#
#
# class ProductListView(ListView):
#     model = Product
#     template_name = 'products/product_list.html'

