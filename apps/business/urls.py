from django.urls import path, include
from rest_framework import routers

from apps.business.views import BussinessWorkViewSet

app_name = "business"

router = routers.DefaultRouter()
router.register(r'business', BussinessWorkViewSet, basename="business")

urlpatterns = [
    path('', include(router.urls)),
]
