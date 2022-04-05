from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta
from api.models import Product


def time_now(request):
    return HttpResponse(datetime.now())

def hours_ahead(request, hours):
    time = datetime.now() + timedelta(hours = hours)
    return HttpResponse(time)
    

def products_list(request):
    # select * from core_product;
    products = Product.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def product_detail(request, product_id):
    # select * from core_product where id = product_id;
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(product.to_json())
