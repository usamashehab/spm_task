from rest_framework import serializers
from spm_task.company.api.serializers import CompanyField, BasicCompanyDataSerializer
from spm_task.core.api.serializers import ApprovalSerializer
from ..models import Client
from spm_task.utils import format_object_data


class ClientSerializer(serializers.ModelSerializer):
    approval = ApprovalSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'company', 'approval']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        company = instance.company
        data['company'] = BasicCompanyDataSerializer(company).data
        return format_object_data(data)
