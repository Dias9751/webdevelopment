from django.shortcuts import render


# Create your views here.
from django.http import HttpResponse, JsonResponse
from hh_back.models import Vacancy, Company
def vacancy_list(request):
    # select * from core_product;
    products = Vacancy.objects.all()
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def vacancy_detail(request, vacancy_id):
    # select * from core_product where id = product_id;
    try:
        product = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)})

    return JsonResponse(product.to_json())

def top10(request):
    products = Vacancy.objects.all().order_by('-salary')[:10]
    products_json = [product.to_json() for product in products]
    return JsonResponse(products_json, safe=False)


def companies_list(request):
    # select * from core_product;
    categories = Company.objects.all()
    categories_json = [categor.to_json() for categor in categories]
    return JsonResponse(categories_json, safe=False)


def company_detail_vacancy(request, companies_id):
    # select * from core_product where id = product_id;
    try:
        categor = Company.objects.get(id=companies_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    produc = categor.vacancy_set.all()
    json_products = [p.to_json() for p in produc]
    return JsonResponse(json_products, safe=False)
   #return JsonResponse(categor.to_json())

def company_detail(request, companies_id):
    # select * from core_product where id = product_id;
    try:
        categor1 = Company.objects.get(id=companies_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)})
    
    return JsonResponse(categor1.to_json())