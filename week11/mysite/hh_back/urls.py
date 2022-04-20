from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token
from hh_back.views import vacancy_list, vacancy_detail, company_detail, company_detail_vacancy, top10, CompanyListAPIView

urlpatterns = [
    path('login/', obtain_jwt_token),
    
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', top10),
    path('companies/', CompanyListAPIView.as_view()),
    path('companies/<int:companies_id>/', company_detail),
    path('companies/<int:companies_id>/vacancies/', company_detail_vacancy)
]

# for views1variant and views2variant
"""urlpatterns = [
    path('vacancies/', vacancy_list),
    path('vacancies/<int:vacancy_id>/', vacancy_detail),
    path('vacancies/top_ten/', top10),
    path('companies/', companies_list),
    path('companies/<int:companies_id>/', company_detail),
    path('companies/<int:companies_id>/vacancies/', company_detail_vacancy)
]"""