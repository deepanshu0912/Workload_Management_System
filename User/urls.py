from django.urls import path
from django.shortcuts import redirect
from .views import (LoginView, LogoutView, UserRegistrationView)

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('signup/', UserRegistrationView.as_view(), name='signup')

]