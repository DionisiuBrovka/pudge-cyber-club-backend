from rest_framework.viewsets import ModelViewSet

from data.models import *
from .serializers import *

class MultiSerializerViewSet(ModelViewSet):
    serializers = { 
        'default': None,
    }

    def get_serializer_class(self):
            return self.serializers.get(self.action,
                        self.serializers['default'])

class ClubViewSet(MultiSerializerViewSet):
    model  = Club
    queryset = Club.objects.all()
    serializers = {
        'list':    ClubListSerializer,
        'detail':  ClubSerializer,
        'default': ClubSerializer,
        # etc.
    }


class PCLevelViewSet(MultiSerializerViewSet):
    model  = PCLevel
    queryset = PCLevel.objects.all()
    serializers = {
        'list':    PCLevelListSerializer,
        'detail':  PCLevelSerializer,
        'default': PCLevelSerializer,
        # etc.
    }


class PCViewSet(MultiSerializerViewSet):
    model  = PC
    queryset = PC.objects.all()
    serializers = {
        'list':    PCListSerializer,
        'detail':  PCSerializer,
        'default': PCSerializer,
        # etc.
    }