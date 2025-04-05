from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Food_Items
from .serializers import Food_ItemsListSerializers
from django.conf import settings

class GetFoodItemsView(ListAPIView):    
    queryset = Food_Items.objects.all()
    serializer_class = Food_ItemsListSerializers