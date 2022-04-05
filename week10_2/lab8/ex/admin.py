from django.contrib import admin

# Register your models here.
from ex.models import Product, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['id', 'category', 'name', 'price', 'description', 'count', 'is_active']

admin.site.register(Category,  CategoryAdmin)
admin.site.register(Product, ArticleAdmin)

