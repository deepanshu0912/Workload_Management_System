from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import UserCredentials
from .serializers import LoginSerializer, UserSerializer
from django.conf import settings

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'User registration successful'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        if('userid' in request.session):
            userid = request.session['userid']
            user = UserCredentials.objects.get(userid=userid)
            return Response({"message" : "User Session Already Exists", "user_id": user.userid}, status=status.HTTP_200_OK)
    
        serializer = LoginSerializer(data=request.data)
        if(serializer.is_valid()):
            userid = serializer.validated_data["userid"]
            password = serializer.validated_data['password']
            request.session["userid"] = userid

            return Response({"message":"Login Successful", "userid":userid}, status=status.HTTP_200_OK)
        
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    def post(self, request):
        if "userid" in request.session:
            request.session.flush()
            response = Response({"message" : "User Logged Out"}, status=status.HTTP_200_OK)
            response.delete_cookie(settings.SESSION_COOKIE_NAME, path = '/')
            return response
        else:
            return Response({"error": "User Session does not exists."}, status=status.HTTP_400_BAD_REQUEST)
