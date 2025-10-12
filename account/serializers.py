from rest_framework import serializers
from django.contrib.auth.models import User
class  RegistrationSeriarizer(serializers.ModelSerializer):
    confirm_password=serializers.CharField(required=True)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password','confirm_password']

    def save(self):
        username=self.validated_data('username')
        email=self.validated_data('email')
        password=self.validated_data('password')
        confirm_password=self.validated_data('confirm_password')
        
        if password !=confirm_password:
            raise serializers.ValidationError({'error' : "password doesn't mactched"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error' : "Email Already exists "})
        
        account=User(username=username,email=email)
        account.set_password(password)
        account.save()
        return account