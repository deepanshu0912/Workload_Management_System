from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserCredentials
from .serializers import UserCredentialsSerializer, LoginSerializer
from django.conf import settings

class LoginView(APIView):
    def post(self, request):
        if('mobile' in request.session):
            mobile = request.session['mobile']
            user = UserCredentials.objects.get(mobile=mobile)
            return Response({"message" : "User Session Already Exists", "user_id": user.mobile}, status=status.HTTP_200_OK)
    
        serializer = LoginSerializer(data=request.data)
        if(serializer.is_valid()):
            mobile = serializer.validated_data["mobile"]
            password = serializer.validated_data['password']
            request.session["mobile"] = mobile

            return Response({"message":"Login Successful", "userid":mobile}, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        if "mobile" in request.session:
            request.session.flush()
            response = Response({"message" : "User Logged Out"}, status=status.HTTP_200_OK)
            response.delete_cookie(settings.SESSION_COOKIE_NAME, path = '/')
            return response
        else:
            return Response({"error": "User Session does not exists."}, status=status.HTTP_400_BAD_REQUEST)
