from rest_framework.viewsets import ModelViewSet

from data.models import *
from .serializers import *

class ClubViewSet(ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubListSerializer


class PCLevelViewSet(ModelViewSet):
    queryset = PCLevel.objects.all()
    serializer_class = PCLevelListSerializer


class PCViewSet(ModelViewSet):
    queryset = PC.objects.all()
    serializer_class = PCListSerializer