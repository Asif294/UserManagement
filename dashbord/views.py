# views.py
from rest_framework import viewsets, filters, pagination
from django.contrib.auth.models import User
from .serializers import UserListSerializer
from rest_framework.permissions import IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from rest_framework.authtoken.models import Token

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
    search_fields = [
        'username',
        'first_name',
        'last_name',
        'email',
        'is_active',
        'is_staff',        
        'is_superuser',
    ]



class ActiveUserCountView(APIView):
    permission_classes = [IsAdminUser]  
    def get(self, request):
        active_user_count = Token.objects.count()
        return Response({"total_logged_in_users": active_user_count})