from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSeriarizer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Registration successful!'})
        return Response(serializer.errors, status=400)
