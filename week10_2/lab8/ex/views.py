from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, JsonResponse
from ex.models import Product, Category
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

def categories_list(request):
    # select * from core_product;
    categories = Category.objects.all()
    categories_json = [categor.to_json() for categor in categories]
    return JsonResponse(categories_json, safe=False)


def category_detail(request, categor_id):
    # select * from core_product where id = product_id;
    try:
        categor = Category.objects.get(id=categor_id)
    except Category.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    produc = categor.product_set.all()
    json_products = [p.to_json() for p in produc]
    return JsonResponse(json_products, safe=False)
   #return JsonResponse(categor.to_json())