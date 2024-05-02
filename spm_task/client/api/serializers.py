from rest_framework import serializers
from spm_task.company.api.serializers import CompanyField
from spm_task.core.api.serializers import ApprovalSerializer
from ..models import Client
from spm_task.utils import format_object_data


class ClientSerializer(serializers.ModelSerializer):
    company = CompanyField(required=True)
    approval = ApprovalSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'company', 'approval']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return format_object_data(data)
