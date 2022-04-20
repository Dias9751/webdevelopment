from rest_framework import serializers
from hh_back.models import Company, Vacancy

 
class CompanySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()

    def create(self, validated_data):
        company = Company.objects.create(name=validated_data['name'])
        return company

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.save()
        return instance


class VacancySerializer2(serializers.ModelSerializer):
    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary')


class CompanySerializer2(serializers.ModelSerializer):
    name = serializers.CharField()

    # products = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # products = serializers.StringRelat    edField(many=True, read_only=True)

    # products = Product2Serializer(many=True, read_only=True)

    class Meta:
        model = Company
        fields = ('id', 'name', 'description', 'city', 'address')
        # read_only_fields = ('name',)


class VacancySerializer(serializers.ModelSerializer):
    company = CompanySerializer2(read_only=True)
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = ('id', 'name', 'description', 'salary', 'company', 'company_id',)