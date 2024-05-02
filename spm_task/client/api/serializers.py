from rest_framework import serializers
from spm_task.company.api.serializers import CompanyField
from spm_task.core.api.serializers import ApprovalSerializer
from ..models import Client


class ClientSerializer(serializers.ModelSerializer):
    company = CompanyField(required=True)
    approval = ApprovalSerializer(read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'name', 'company', 'approval']
