from rest_framework import serializers
from .models import UserCredentials, User


class UserCredentialsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredentials
        fields = ['userid', 'password']

    def validate_userid(self, userid):
        if UserCredentials.objects.filter(userid=userid).exists():
            raise serializers.ValidationError('User does not exists.')
        if len(userid) < 6:
            raise serializers.ValidationError('Userid must contain atleast 6 characters.')
        
        return userid
    
    def validate_password(self, password):
        if(len(password) < 8):
            raise serializers.ValidationError("Password length must be between at least 8 characters.")
        return password
    
    def create(self, validated_data):
        return super().create(validated_data)


class UserSerializer(serializers.ModelSerializer):
    user_credentials = UserCredentialsSerializer()

    class Meta:
        model = User
        fields = [
            'name',
            'user_credentials',
            'mobile',
            'user_type',
            'address',
        ]

    def validate_mobile(self, value):
        if User.objects.filter(mobile=value).exists():
            raise serializers.ValidationError('Mobile number already registered.')
        if len(value) != 10 or not value.isdigit():
            raise serializers.ValidationError('Mobile number must be a 10-digit number.')
        return value

    def validate_user_type(self, value):
        user_type_choices = [('Customer', 'Customer'),('Chef', 'Chef')]
        valid_user_type = [choice[0] for choice in user_type_choices]
        if value not in valid_user_type:
            raise serializers.ValidationError('Invalid User type.')
        return value

    def create(self, validated_data):
        user_credentials_data = validated_data.pop('user_credentials')

        user_credentials_serializer = UserCredentialsSerializer(data=user_credentials_data)
        user_credentials_serializer.is_valid(raise_exception=True)
        user_credentials = user_credentials_serializer.save()

        # Create Voter instance
        user = User.objects.create(
            user_credentials=user_credentials,
            **validated_data
        )
        return user

    
class LoginSerializer(serializers.Serializer):
    userid = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        userid = data.get('userid')
        password = data.get('password')

        if not userid or not password:
            raise serializers.ValidationError('Both mobile and password are required.')
        try:
            user_credentials = UserCredentials.objects.get(userid=userid)
            
        except UserCredentials.DoesNotExist:
            raise serializers.ValidationError('User does not exists.')

        if password != user_credentials.password:
            raise serializers.ValidationError('Invalid password.')

        data['user_credentials'] = user_credentials
        return data

