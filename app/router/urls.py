from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import *
from djoser.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'clubs', ClubViewSet)
router.register(r'levels', PCLevelViewSet)
router.register(r'computers', PCViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
