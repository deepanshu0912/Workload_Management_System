from django.shortcuts import render
from django.http import HttpResponse

def temp_view(request):
    return HttpResponse("Hello World")