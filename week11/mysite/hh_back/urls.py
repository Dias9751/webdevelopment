from django.urls import path
from hh_back.views import vacancy_list, vacancy_detail, companies_list, company_detail, company_detail_vacancy, top10

urlpatterns = [
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', top10),
    path('companies/', companies_list),
    path('companies/<int:companies_id>/', company_detail),
    path('companies/<int:companies_id>/vacancies/', company_detail_vacancy)
]