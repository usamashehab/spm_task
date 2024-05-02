from rest_framework import serializers


def valid_field_existing(data, field_name):
    if not data:
        raise serializers.ValidationError(
            f"this field [{field_name}] is requried")
