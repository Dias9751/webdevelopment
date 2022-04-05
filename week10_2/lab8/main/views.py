# Create your views here.
from django.http import HttpResponse, JsonResponse

products = [
    {
        'id': i,
        'name': f'Product {i}',
        'price': i * 1000
    } for i in range(1, 11)
]

def products_list(request):
    return JsonResponse(products, safe=False)


def product_detail(request, product_id):
    for product in products:
        if product['id'] == product_id:
            return JsonResponse(product)
    return JsonResponse({'message': 'Product with selected ID not found'})