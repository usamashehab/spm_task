from rest_framework import serializers


class ApprovalSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    status = serializers.CharField()
