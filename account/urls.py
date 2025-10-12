from django.urls import path,include
from .import views
urlpatterns = [
 
 path('register/',views.UserRegistrationApiView.as_view(),name='register')
   
]