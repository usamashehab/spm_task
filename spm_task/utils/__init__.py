from rest_framework.response import Response
from typing import Dict
from rest_framework.pagination import LimitOffsetPagination


def format_object_data(data):
    approval = data.pop('approval', None)
    formatted_data = {
        "data": data,
        "approval": approval
    }
    return formatted_data
