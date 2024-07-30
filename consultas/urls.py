from rest_framework import routers
from django.urls import path, include
from .views import EstudiantesViewSet

router = routers.DefaultRouter()
router.register(r'estudiantes', EstudiantesViewSet)

urlpatterns = [
    path('', include(router.urls))
]
