from rest_framework import serializers
from django.contrib.auth.models import User

class RegistrationSeriarizer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']

    def save(self):
        username = self.validated_data['username']
        first_name=self.validated_data['first_name']
        last_name=self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        confirm_password = self.validated_data['confirm_password']

        if password != confirm_password:
            raise serializers.ValidationError({'error': "Passwords don't match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})

        account = User(username=username,first_name=first_name,last_name=last_name, email=email  )
        account.set_password(password)
        account.is_active=False
        account.save()
        return account
 
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)
 
    class Meta:
        model = User
        fields = ['username', 'password']


class UserProfileSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password']
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, data):
       
        password = data.get('password')
        confirm_password = data.get('confirm_password')
        if password and confirm_password and password != confirm_password:
            raise serializers.ValidationError("Passwords do not match.")
        return data

    def update(self, instance, validated_data):
        validated_data.pop('confirm_password', None)
        password = validated_data.pop('password', None)

    
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)
        instance.save()
        return instance

