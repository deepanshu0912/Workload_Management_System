from rest_framework import serializers
from .models import UserCredentials

class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredentials
        fields = ['mobile', 'password']

    def validate_mobile(self, mobile):
        if UserCredentials.objects.filter(mobile=mobile).exists():
            raise serializers.ValidationError('Mobile number already exists.')
        if len(mobile) != 10:
            raise serializers.ValidationError('Mobile Number must be 10 digits')
        
        return mobile
    
    def validate_password(self, password):
        if(len(password) < 8):
            raise serializers.ValidationError("Password length must be between at least 8 characters.")
        return password
    
    def create(self, validated_data):
        return super().create(validated_data)
    
class LoginSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        mobile = data.get('mobile')
        password = data.get('password')

        if not mobile or not password:
            raise serializers.ValidationError('Both mobile and password are required.')

        try:
            user_credentials = UserCredentials.objects.get(mobile=mobile)
        except UserCredentials.DoesNotExist:
            raise serializers.ValidationError('User does not exists.')

        if password != user_credentials.password:
            raise serializers.ValidationError('Invalid password.')

        data['user_credentials'] = user_credentials
        return data

