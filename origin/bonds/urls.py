from django.urls import path, include
from bonds.views import HelloWorld
from rest_framework.routers import DefaultRouter

from bonds.views import BondViewSet


router = DefaultRouter()
router.register('bond', BondViewSet)


urlpatterns = [
    path('', include(router.urls)),
]