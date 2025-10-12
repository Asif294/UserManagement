from django.urls import path,include
from .import views
urlpatterns = [
 
 path('register/',views.UserRegistrationApiView.as_view(),name='register'),
 path("login/", views.UserLoginApiView.as_view(), name="login"),
 path('active/<uid64>/<token>/',views.activate,name='activate')
   
]