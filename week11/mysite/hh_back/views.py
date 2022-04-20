import json

from rest_framework.permissions import IsAuthenticated

from django.shortcuts import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from hh_back.models import Company, Vacancy
from hh_back.serializers import CompanySerializer, CompanySerializer2, VacancySerializer, VacancySerializer2

class CompanyListAPIView(APIView):
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer2(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CompanySerializer2(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    permission_classes = (IsAuthenticated,)

@csrf_exempt
def company_detail(request, companies_id):
    try:
        company = Company.objects.get(id=companies_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    if request.method == 'GET':
        serializer = CompanySerializer2(company)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CompanySerializer2(instance=company, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors)
    elif request.method == 'DELETE':
        company.delete()
        return JsonResponse({'message': 'deleted'}, status=204)


@csrf_exempt
def vacancy_list(request):
    vacancies = Vacancy.objects.all()
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def vacancy_detail(request, vacancy_id):
    try:
        vacancy = Vacancy.objects.get(id=vacancy_id)
    except Vacancy.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    serializer = VacancySerializer(vacancy)
    return JsonResponse(serializer.data)

@csrf_exempt
def top10(request):
    vacancies = Vacancy.objects.all().order_by('-salary')[:10]
    serializer = VacancySerializer(vacancies, many=True)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def company_detail_vacancy(request, companies_id):
    try:
        company = Company.objects.get(id=companies_id)
    except Company.DoesNotExist as e:
        return JsonResponse({'message': str(e)}, status=400)

    produc = company.vacancy_set.all()
    serializer = VacancySerializer(produc, many = True)
    return JsonResponse(serializer.data, safe = False)