from rest_framework.viewsets import ModelViewSet

from data.models import *
from .serializers import *
from .permission import *

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
    permission_classes = (AppBasePermissionClass,)
    serializers = {
        'list':    ClubListSerializer,
        'detail':  ClubSerializer,
        'default': ClubSerializer,
        # etc.
    }


class PCLevelViewSet(MultiSerializerViewSet):
    model  = PCLevel
    queryset = PCLevel.objects.all()
    permission_classes = (AppBasePermissionClass,)
    serializers = {
        'list':    PCLevelListSerializer,
        'detail':  PCLevelSerializer,
        'default': PCLevelSerializer,
        # etc.
    }


class PCViewSet(MultiSerializerViewSet):
    model  = PC
    queryset = PC.objects.all()
    permission_classes = (AppBasePermissionClass,)
    serializers = {
        'list':    PCListSerializer,
        'detail':  PCSerializer,
        'default': PCSerializer,
        # etc.
    }