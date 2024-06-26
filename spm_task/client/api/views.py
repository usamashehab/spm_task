from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from ..models import Client
from .serializers import ClientSerializer
from rest_framework.response import Response
from spm_task.utils import query_debugger


class ClientView(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin
                 ):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset().select_related('approval', 'company')
        return queryset

    @query_debugger
    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response({'message': 'No clients found'}, status=status.HTTP_400_BAD_REQUEST)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
