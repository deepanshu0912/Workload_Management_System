from django.contrib import admin
from .models import UserCredentials, User

admin.site.register(UserCredentials)
admin.site.register(User)