from rest_framework import viewsets, mixins, status
from rest_framework.permissions import IsAuthenticated
from ..models import Company
from .serializers import CompanySerializer
from rest_framework.response import Response


class CompanyView(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin
                  ):
    permission_classes = [IsAuthenticated]
    serializer_class = CompanySerializer
    queryset = Company.objects.all()

    def get_queryset(self):
        queryset = super().get_queryset().select_related(
            'small_business', 'startup', 'corporate', 'approval')
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response({'message': 'No companies found'}, status=status.HTTP_400_BAD_REQUEST)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
