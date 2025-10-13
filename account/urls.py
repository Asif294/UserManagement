from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter


urlpatterns = [

 path('register/',views.UserRegistrationApiView.as_view(),name='register'),
 path("login/", views.UserLoginApiView.as_view(), name="login"),
 path("logout/", views.UserLogoutApiView.as_view(), name="logout"),
 path('active/<uid64>/<token>/',views.activate,name='activate')
   
]