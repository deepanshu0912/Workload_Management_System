from django.urls import path
# from .views import (LoginView, LogoutView, UserRegistrationView)
from .views import temp_view

urlpatterns = [
    path('temp/', temp_view, name='temp'),
]