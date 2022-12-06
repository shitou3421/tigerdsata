from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from apps.business.models import BusinessWork
from apps.business.serializers import BusinessWorkSerializer


class BussinessWorkViewSet(viewsets.ModelViewSet):
    queryset = BusinessWork.objects.all().order_by("id")
    serializer_class = BusinessWorkSerializer
    filter_backends = [DjangoFilterBackend]
    ordering_fields = "__all__"

