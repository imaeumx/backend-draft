from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import StudentViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
    path('register/', views.register_user, name='register_user'),
]