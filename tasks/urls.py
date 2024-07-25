from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import TaskView

router = routers.DefaultRouter()
router.register(r'tasks', TaskView)

urlpatterns = [
    path('', include(router.urls)),
]
