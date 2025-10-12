from rest_framework.views import APIView
from . import serializers
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes

#####  for mail verification 
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

class UserRegistrationApiView(APIView):
    serializer_class = serializers.RegistrationSeriarizer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
            token =default_token_generator.make_token (user)
            uid=urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/account/active/{uid}/{token}"
            email_subject="Confirm Your Email"
            email_body= render_to_string('confirm_email.html',{'confirm_link':confirm_link})
            email=EmailMultiAlternatives(email_subject,'',to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()
            return Response({'message': 'Chack your email for confirmation'})
        return Response(serializer.errors, status=400)
