from django.contrib import admin

# Register your models here.
from hh_back.models import Vacancy, Company

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'city', 'address']

class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'company', 'name', 'description', 'salary' ]

admin.site.register(Company,  CompanyAdmin)
admin.site.register(Vacancy, VacancyAdmin)