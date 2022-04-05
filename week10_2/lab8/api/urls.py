from django.urls import path
from api.views import time_now, hours_ahead, products_list, product_detail

urlpatterns = [
    path('time/', time_now),
    path('time/plus/<int:hours>/', hours_ahead),
    path('products/', products_list),
    path('products/<int:product_id>/', product_detail)
]