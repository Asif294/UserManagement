from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet,ActiveUserCountView

router = DefaultRouter()
router.register('users', UserViewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    path('login-users/', ActiveUserCountView.as_view(), name='login-users'),
]

