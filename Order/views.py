from django.shortcuts import render
from django.db import models
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import status
from .models import Orders, Order_Items
from django.conf import settings

# class getNextOrderItem(models.Model):
#     def post(self, request):
#         pass
#         #order_items = Order_Items.objects.all()