from rest_framework import serializers
from .models import StudentModel
from django.contrib.auth import authenticate

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = StudentModel
        fields = ('email', 'full_name', 'password', 'bio', 'avatar', 'phone_number')

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = StudentModel(**validated_data)
        user.set_password(password)
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        user = authenticate(email=data['email'], password=data['password'])
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Invalid email or password")
