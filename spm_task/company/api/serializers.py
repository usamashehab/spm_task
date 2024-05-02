from rest_framework import serializers, exceptions
from ..models import Company, SmallBusiness, Startup, Corporate
from .utils import valid_field_existing
from spm_task.core.api.serializers import ApprovalSerializer
from collections import OrderedDict
from spm_task.utils import format_object_data


class SmallBusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = SmallBusiness
        fields = ['num_employess', 'industry']


class StartupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Startup
        fields = ['funding_rounds', 'founders']


class CoroprateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Corporate
        fields = ['location']


class CompanySerializer(serializers.ModelSerializer):
    small_business = SmallBusinessSerializer(required=False)
    startup = StartupSerializer(required=False)
    corporate = CoroprateSerializer(required=False)
    approval = ApprovalSerializer(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'type', 'name', 'approval',
                  'small_business', 'startup', 'corporate']

    def create(self, validated_data):
        company_type = validated_data.get('type')
        company_profile_serializer = None
        if company_type == Company.Type.SMALL_BUSINESS:
            data = validated_data.pop('small_business', None)
            valid_field_existing(data, 'small_business')
            company_profile_serializer = SmallBusinessSerializer(data=data)
        elif company_type == Company.Type.STARTUP:
            data = validated_data.pop('startup', None)
            valid_field_existing(data, 'startup')
            company_profile_serializer = StartupSerializer(data=data)
        elif company_type == Company.Type.CORPORATE:
            data = validated_data.pop('corporate', None)
            valid_field_existing(data, 'corporate')
            company_profile_serializer = CoroprateSerializer(data=data)

        company = Company.objects.create(**validated_data)
        company_profile_serializer.is_valid(raise_exception=True)
        company_profile_serializer.save(company=company)
        return company

    def to_representation(self, instance):
        data = super().to_representation(instance)
        for field in ['small_business', 'startup', 'corporate']:
            if data[field] is None:
                data.pop(field)
        return format_object_data(data)


class CompanyField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        return Company.objects.all()

    def to_internal_value(self, data):
        try:
            return super().to_internal_value(data)
        except exceptions.ValidationError:
            raise exceptions.ValidationError(
                "Company with this ID does not exist")

    def to_representation(self, value):
        pk = super().to_representation(value)
        try:
            company = Company.objects.get(pk=pk)
            data = {
                'id': company.id,
                'name': company.name,
                'type': company.type,
            }
            return data
        except Company.DoesNotExist:
            return None

    def get_choices(self, cutoff=None):
        queryset = self.get_queryset()
        if queryset is None:
            return {}
        return OrderedDict([(item.id, str(item)) for item in queryset])
