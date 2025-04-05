from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('User.urls')),
    path('food/', include('Food.urls')),
    path('order/', include('Order.urls')),
]
