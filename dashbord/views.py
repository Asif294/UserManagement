from rest_framework import viewsets, filters, pagination
from django.contrib.auth.models import User
from .serializers import UserListSerializer
from rest_framework.permissions import IsAdminUser

class UserViewPagination(pagination.PageNumberPagination):
    page_size = 100               
    page_query_param = 'page'    
    page_size_query_param = 'page_size'  
    max_page_size = 10000000         

class UserViewSet(viewsets.ModelViewSet):  
    permission_classes = [IsAdminUser] 
    queryset = User.objects.all().order_by('id')
    serializer_class = UserListSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = UserViewPagination
    search_fields = ['username', 'first_name', 'last_name', 'email']
