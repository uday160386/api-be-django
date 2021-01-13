from django.urls import include, path
from rest_framework import routers

from app.views import MedicineViewSet

router = routers.DefaultRouter()
router.register('medicines', MedicineViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
